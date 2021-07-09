from django.db import models
from uuid import uuid4


class Gender(models.Model):
    """ 性別 """
    id = models.CharField(max_length=255, default=uuid4, primary_key=True, editable=False)
    gender = models.CharField('性別', max_length=10)

    def __str__(self):
        return f'{self.id} : {self.gender}'
