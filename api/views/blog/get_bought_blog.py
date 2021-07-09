from blog.serializers import BlogBuySerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from blog.models import PurchaseHistory
from rest_framework.response import Response
from rest_framework import status


class GetBoughtView(APIView):
    serializer_class = BlogBuySerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        purchase_history = PurchaseHistory.objects.filter(purchase=request.data['purchase'], blog=request.data['blog'])
        if len(purchase_history) == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST,)
        return Response(status=status.HTTP_200_OK,)
