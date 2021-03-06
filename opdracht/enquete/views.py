from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, QueryDict

from .models import Quiz, Antwoord

# Create your views here.
def index(request):
    return render(request, 'enquete/index.html')

def quiz(request):
    quiz_list = Quiz.objects.all()
    return render(request, 'quiz.html', context={'quiz_list': quiz_list})

def quiz_maken(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    vragenlist = quiz.vraag_set.all()
    return render(request, 'quiz_maken.html', {'vraag_list': vragenlist, 'quiz': quiz})

def quiz_resultaat(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    vragen_list = quiz.vraag_set.all()
    user_antwoorden = []
    max_score = 0
    score = 0

    q = QueryDict()
    q = request.POST
    user_antwoorden.extend(q.items())
    user_antwoorden.pop(0)
    
    user_antwoord_ids = [antwoord[0] for antwoord in user_antwoorden]
    
    user_antwoord_ids = [id for id in user_antwoord_ids if str.isdigit(id)]

    # Map list naar integers
    user_antwoord_ids = list(map(int, user_antwoord_ids))

    # Check of de vraag een ja/nee vraag is en indien ja, vervang vraag id naar antwoord id als het gegeven antwoord juist is.
    for id in user_antwoord_ids:
        for vraag in vragen_list:
            if vraag.id == id and vraag.vraag_type == 'jaNee':
                user_antwoord = request.POST.get(str(id))
                juiste_antwoord = vraag.antwoord_set.get(antwoord_juist=True)
                if user_antwoord.lower() == juiste_antwoord.antwoord_tekst.lower():
                    user_antwoord_ids.remove(id)
                    user_antwoord_ids.append(juiste_antwoord.id)
                else:
                    user_antwoord_ids.remove(id)
    
    juiste_antwoorden = Antwoord.objects.filter(antwoord_juist=True)

    # Totale score berekenen per quiz.
    for vraag in vragen_list:
        juiste_antwoorden_per_quiz = vraag.antwoord_set.filter(antwoord_juist=True)
        
        for antwoord in juiste_antwoorden_per_quiz:
            max_score += antwoord.antwoord_score
    
    def get_antwoord_ids():
        list_ids = []
        for vraag in vragen_list:
            juiste_antwoorden = vraag.antwoord_set.filter(antwoord_juist=True)
            for antwoord in juiste_antwoorden:
                list_ids.append(antwoord.id)
        return list_ids

    juiste_antwoorden_ids = get_antwoord_ids()

    # Vergelijken tussen gegeven antwoorden en de juiste antwoorden.
    matches = set(user_antwoord_ids).intersection(juiste_antwoorden_ids)

    for match in matches:
        vraag = Antwoord.objects.get(id=match).vraag
        juist_antwoord = Antwoord.objects.get(id=match)

        if vraag.vraag_type == 'open':
            user_value = q.get(str(match))

            if user_value.lower() == juist_antwoord.antwoord_tekst.lower():
                score += juist_antwoord.antwoord_score
        else:
            score += juist_antwoord.antwoord_score

    return render(request, 'resultaat.html', {'user_score': score, 'max_score': max_score, 'max_score_helft': max_score / 2})