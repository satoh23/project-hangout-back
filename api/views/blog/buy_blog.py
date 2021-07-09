from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from blog.serializers import BlogBuySerializer
from blog.models import PurchaseHistory, BlogDetail
from accounts.models import CustomUser
import math


class BuyBlogView(generics.CreateAPIView):
    queryset = PurchaseHistory.objects.all()
    serializer_class = BlogBuySerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        blog = BlogDetail.objects.get(pk=request.data['blog'])
        user = CustomUser.objects.get(pk=request.data['purchase'])
        author = blog.author_id
        user.own_point -= blog.price
        author.own_point += math.floor(blog.price/11*10)
        user.save()
        author.save()
        return self.create(request, *args, **kwargs)
