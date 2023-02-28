from django.http import HttpRequest
from django.shortcuts import render
from .models import Film

def index(request: HttpRequest):
    films = Film.objects.all()
    chunks = []
    for i in range(0, len(films), 4):
        chunks.append(films[i:i+4])
    context = {'films_chunked': chunks}
    return render(request, 'films/index.html', context=context)
