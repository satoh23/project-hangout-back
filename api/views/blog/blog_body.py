from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from blog.serializers import BlogBodySerializer
from blog.models import BlogDetail


class BlogBodyView(generics.RetrieveAPIView):
    queryset = BlogDetail.objects.all()
    serializer_class = BlogBodySerializer
    permission_classes = (IsAuthenticated,)
