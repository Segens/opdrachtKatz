from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'enquete/index.html')

def register(request):
    return render(request, 'enquete/register.html')