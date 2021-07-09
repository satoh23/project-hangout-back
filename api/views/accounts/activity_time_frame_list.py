from rest_framework.permissions import AllowAny
from rest_framework import generics
from accounts.models import ActivityTimeFrame
from accounts.serializers import TimeListSerializer


class TimeListView(generics.ListAPIView):
    queryset = ActivityTimeFrame.objects.all()
    serializer_class = TimeListSerializer
    permission_classes = (AllowAny,)
