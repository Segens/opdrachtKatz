from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Quiz

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
    return render(request, 'resultaat.html', {})