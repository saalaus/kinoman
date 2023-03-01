from django.contrib import admin
from .models import Film, Genre

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
