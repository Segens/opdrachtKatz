from django.db import models

# Create your models here.
class Quiz(models.Model):
    class Meta:
        verbose_name_plural = 'quizzen'

    quiz_titel = models.CharField(max_length=100)
    quiz_beschrijving = models.TextField()

    def __str__(self):
        return self.quiz_titel
    

class Vraag(models.Model):
    class Meta:
        verbose_name_plural = 'vragen'

    TYPES = (
        ('open', 'Open'),
        ('multichoice', 'Multiple Choice'),
        ('jaNee', 'Ja/Nee'),
    )
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, default=1)
    vraag_tekst = models.CharField(max_length=200)
    vraag_type = models.CharField(max_length=50, choices=TYPES)
    vraag_score = models.FloatField()
    vraag_meerdere = models.BooleanField(verbose_name='Meerdere juiste antwoorden')
    
    def __str__(self):
        return self.vraag_tekst + ' | ' + self.vraag_type
    
class Antwoord(models.Model):
    class Meta:
        verbose_name_plural = 'antwoorden'

    vraag = models.ForeignKey(Vraag, on_delete=models.CASCADE)
    antwoord_tekst = models.CharField(max_length=200)
    antwoord_juist = models.BooleanField()

    def __str__(self):
        return self.antwoord_tekst
    