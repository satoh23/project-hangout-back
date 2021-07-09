from django.db import models


class Genre(models.Model):
    """ブログのジャンル"""
    genre = models.CharField('ジャンル', max_length=20)

    def __str__(self):
        return f'{self.id}: {self.genre}'
