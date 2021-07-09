from django.db import models
from accounts.models import CustomUser
from django.utils import timezone


class MessageBox(models.Model):
    """メッセージ"""
    male_id = models.ForeignKey(CustomUser, verbose_name='男性側', on_delete=models.PROTECT, related_name='male_user')
    female_id = models.ForeignKey(CustomUser, verbose_name='女性側', on_delete=models.PROTECT, related_name='female_user')
    message = models.TextField('メッセージ')
    did_read = models.BooleanField(verbose_name='既読', default=False, blank=True)

    created_date = models.DateTimeField('登録日', default=timezone.now)

    def __str__(self):
        return f'{self.id}: {self.message}'
