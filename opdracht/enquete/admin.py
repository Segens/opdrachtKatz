from django.contrib import admin

from .models import Vraag, Antwoord

# Register your models here.
admin.site.register(Vraag)
admin.site.register(Antwoord)