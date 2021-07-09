from rest_framework import serializers
from blog.models import BlogDetail

from rest_framework.serializers import SerializerMethodField


class BlogBodySerializer(serializers.ModelSerializer):
    """各ブログの詳細取得に使う"""

    class Meta:
        model = BlogDetail
        fields = ('body',)
        read_only_fields = ('body',)
