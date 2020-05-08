from django.urls import path, include, reverse
from django.views.generic.base import TemplateView

from . import views

app_name = 'enquete'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz/<int:quiz_id>', views.quiz_maken, name='quizStart'),
]
