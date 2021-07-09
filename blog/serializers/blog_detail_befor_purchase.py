from rest_framework import serializers
from blog.models import BlogDetail
import urllib.parse

from rest_framework.serializers import SerializerMethodField


class BlogDetailBeforPurchaseSerializer(serializers.ModelSerializer):
    """各ブログの詳細取得に使う"""
    author = SerializerMethodField()
    author_profile = SerializerMethodField()
    author_icon = SerializerMethodField()
    genre = SerializerMethodField()

    class Meta:
        model = BlogDetail
        fields = ('id', 'thumbnail', 'title', 'summary', 'price', 'author', 'author_profile', 'author_icon',
                  'genre', 'author_id', 'genre_id', 'created_date')
        read_only_fields = ('id', 'thumbnail', 'title', 'summary', 'price', 'author', 'author_profile', 'author_icon',
                            'genre', 'author_id', 'genre_id', 'created_date')

    def get_author(self, obj):
        try:
            author_name = obj.author_id.user_name
            return author_name
        except:
            return None

    def get_author_profile(self, obj):
        try:
            author_profile = obj.author_id.user_profile
            return author_profile
        except:
            return None

    def get_author_icon(self, obj):
        try:
            icon = urllib.parse.quote(str(obj.author_id.user_icon))
            return icon
        except:
            return None

    def get_genre(self, obj):
        try:
            genre_name = obj.genre_id.genre
            return genre_name
        except:
            return None
