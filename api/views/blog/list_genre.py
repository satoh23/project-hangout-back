from rest_framework.permissions import AllowAny
from rest_framework import generics
from blog.serializers import GenreListSerializer
from blog.models import Genre


class ListGenreView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreListSerializer
    permission_classes = (AllowAny,)
