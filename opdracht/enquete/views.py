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
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    vragen_list = quiz.vraag_set.all()
    user_antwoorden = []
    juiste_ids = []
    max_score = 0.0
    score = 0.0

    # Loop die alle data uit het post request haalt en deze in een list stopt.
    for data in request.POST:
        user_antwoorden.append(data)
    
    # Verwijdert de csrftoken uit de list.
    user_antwoorden.pop(0)

    # Convert alle strings in de lijst naar integers
    user_antwoorden = list(map(int, user_antwoorden))

    print(user_antwoorden)

    for vraag in vragen_list:
        for juist_antwoord in vraag.antwoord_set.filter(antwoord_juist=True):
            juiste_ids.append(juist_antwoord.id)

    print(juiste_ids)

    matches = set(user_antwoorden).intersection(juiste_ids)
    print(matches)

    for id in juiste_ids:
        antwoord = get_object_or_404(Antwoord, id=id)

        if antwoord.vraag.vraag_meerdere:
            max_score += antwoord.vraag.vraag_score / 2
        else:
            max_score += antwoord.vraag.vraag_score

    for id in matches:
        antwoord = get_object_or_404(Antwoord, id=id)

        if antwoord.vraag.vraag_meerdere:
            score += antwoord.vraag.vraag_score / 2
        else:
            score += antwoord.vraag.vraag_score

    return render(request, 'resultaat.html', {'user_score': score, 'max_score': max_score})