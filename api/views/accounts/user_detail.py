from rest_framework.permissions import AllowAny
from rest_framework import generics
from accounts.serializers import UserDetailSerializer
from accounts.models import CustomUser


class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (AllowAny,)
