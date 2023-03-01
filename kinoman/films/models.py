from django.db import models

class Genre(models.Model):
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    name = models.CharField(max_length=30, verbose_name='Название')

    def __str__(self) -> str:
        return self.name

class Film(models.Model):
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    poster = models.ImageField(upload_to = 'posters', verbose_name='Постер')
    genre = models.ManyToManyField(Genre)
    premier_russia = models.DateField(verbose_name='Премьера в России')
    premier_word = models.DateField(verbose_name='Премьера в мире')

    def __str__(self) -> str:
        return self.name
