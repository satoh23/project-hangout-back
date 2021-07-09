from rest_framework import serializers
from blog.models import PurchaseHistory


class BlogBuySerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseHistory
        fields = ('purchase', 'blog')
