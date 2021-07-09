from rest_framework import serializers
from blog.models import Genre


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'genre')
