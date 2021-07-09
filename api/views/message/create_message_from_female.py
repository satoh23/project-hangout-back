from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from message.serializers import CreateMessageSerializer
from message.models import MessageBox


class CreateMessageFromFemaleView(generics.CreateAPIView):
    queryset = MessageBox.objects.all()
    serializer_class = CreateMessageSerializer
    permission_classes = (IsAuthenticated,)
