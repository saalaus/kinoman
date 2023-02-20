from django.shortcuts import render
from .models import Film

def index(request):
    context = {'film': Film.objects.get(pk=1)}
    return render(request, 'films/index.html')
