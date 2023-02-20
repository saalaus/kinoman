from django.contrib import admin
from .models import Film

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
