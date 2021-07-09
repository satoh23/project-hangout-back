from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from blog.serializers import BlogDetailSerializer
from blog.models import BlogDetail


class CreateBlogView(generics.CreateAPIView):
    queryset = BlogDetail.objects.all()
    serializer_class = BlogDetailSerializer
    permission_classes = (IsAuthenticated,)
