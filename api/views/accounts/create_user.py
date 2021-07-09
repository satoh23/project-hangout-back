from rest_framework import generics
from rest_framework.permissions import AllowAny

from accounts.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
