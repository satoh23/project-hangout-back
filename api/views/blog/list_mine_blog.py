from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from blog.serializers import BlogDetailBeforPurchaseSerializer
from blog.models import BlogDetail


class ListMineBlogView(generics.ListAPIView):
    queryset = BlogDetail.objects.all()
    serializer_class = BlogDetailBeforPurchaseSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return BlogDetail.objects.filter(author_id=self.request.user)
