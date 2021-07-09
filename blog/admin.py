from django.contrib import admin
from blog.models import BlogDetail, Genre, PurchaseHistory
# Register your models here.

admin.site.register(BlogDetail)
admin.site.register(Genre)
admin.site.register(PurchaseHistory)
