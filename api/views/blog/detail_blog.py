from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from blog.serializers import RoBlogDetailSerializer
from blog.models import BlogDetail


class DetailBlogView(generics.RetrieveAPIView):
    queryset = BlogDetail.objects.all()
    serializer_class = RoBlogDetailSerializer
    permission_classes = (IsAuthenticated,)
