from django.db import models

# Create your models here.
class Vraag(models.Model):
    class Meta:
        verbose_name_plural = 'vragen'
    TYPES = (
        ('open', 'Open'),
        ('multichoice', 'Multiple Choice'),
        ('jaNee', 'Ja/Nee'),
    )

    vraag_tekst = models.CharField(max_length=200)
    vraag_type = models.CharField(max_length=50, choices=TYPES)
    vraag_score = models.FloatField()
    
    def __str__(self):
        return self.vraag_tekst
    
class Antwoord(models.Model):
    vraag = models.ForeignKey(Vraag, on_delete=models.CASCADE)
    antwoord_open = models.CharField(max_length=200)
    antwoord_multi = models.CharField(max_length=250)
    antwoord_ja_nee = models.BooleanField()