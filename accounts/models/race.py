from django.db import models


class Race(models.Model):
    """ ユーザーのタイプ """

    race = models.CharField('タイプ', max_length=30)

    def __str__(self):
        return self.race
