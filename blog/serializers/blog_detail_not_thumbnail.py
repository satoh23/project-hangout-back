from rest_framework import serializers
from blog.models import BlogDetail


class BlogDetailNotThumbnailSerializer(serializers.ModelSerializer):
    """ブログの作成、編集でサムネイルが存在しない場合に使う(これを使わないとBadRequestになる)"""

    class Meta:
        model = BlogDetail
        fields = ('title', 'summary', 'body', 'price', 'author_id', 'genre_id')
