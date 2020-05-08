from django.contrib import admin

from .models import Vraag, Antwoord, Quiz

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Vraag)
admin.site.register(Antwoord)