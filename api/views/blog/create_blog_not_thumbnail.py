from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from blog.serializers import BlogDetailNotThumbnailSerializer
from blog.models import BlogDetail


class CreateBlogNotThumbnailView(generics.CreateAPIView):
    queryset = BlogDetail.objects.all()
    serializer_class = BlogDetailNotThumbnailSerializer
    permission_classes = (IsAuthenticated,)
