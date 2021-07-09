from django.db import models


class State(models.Model):
    """ ユーザーの状態(ログイン中など) """

    state = models.CharField('状態', max_length=30)

    def __str__(self):
        return self.state
