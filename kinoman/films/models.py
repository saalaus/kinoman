from django.db import models

class Film(models.Model):
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    poster = models.ImageField(upload_to = 'posters', verbose_name='Постер')

    def __str__(self) -> str:
        return self.name
