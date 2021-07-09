from rest_framework.permissions import AllowAny
from rest_framework import generics
from blog.serializers import BlogDetailBeforPurchaseSerializer
from blog.models import BlogDetail


class ListBlogView(generics.ListAPIView):
    queryset = BlogDetail.objects.all()
    serializer_class = BlogDetailBeforPurchaseSerializer
    permission_classes = (AllowAny,)
