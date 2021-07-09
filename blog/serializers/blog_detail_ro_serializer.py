from rest_framework import serializers
from blog.models import BlogDetail

from rest_framework.serializers import SerializerMethodField


class RoBlogDetailSerializer(serializers.ModelSerializer):
    """各ブログの詳細取得に使う"""
    author = SerializerMethodField()
    genre = SerializerMethodField()

    class Meta:
        model = BlogDetail
        fields = ('id', 'thumbnail', 'title', 'summary', 'body', 'author', 'genre',
                  'author_id', 'genre_id', 'created_date')
        read_only_fields = ('id', 'thumbnail', 'title', 'summary', 'body', 'author', 'genre',
                            'author_id', 'genre_id', 'created_date')

    def get_author(self, obj):
        try:
            author_name = obj.author_id.user_name
            return author_name
        except:
            author_name = None
            return author_name

    def get_genre(self, obj):
        try:
            genre_name = obj.genre_id.genre
            return genre_name
        except:
            genre_name = None
            return genre_name