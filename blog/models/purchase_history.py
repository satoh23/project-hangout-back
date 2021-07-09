from django.db import models
from accounts.models import CustomUser
from .blog_detail import BlogDetail
from django.utils import timezone


class PurchaseHistory(models.Model):
    """購入者のリスト"""
    purchase = models.ForeignKey(CustomUser, verbose_name='購入者', on_delete=models.PROTECT)
    blog = models.ForeignKey(BlogDetail, verbose_name='ブログ', on_delete=models.PROTECT)
    is_like = models.BooleanField(verbose_name='いいね', default=False)

    created_date = models.DateTimeField('登録日', default=timezone.now)

    def __str__(self):
        return f'{self.blog}: {self.created_date}'
