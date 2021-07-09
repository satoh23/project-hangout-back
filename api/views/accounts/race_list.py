from rest_framework.permissions import AllowAny
from rest_framework import generics
from accounts.models import Race
from accounts.serializers import RaceListSerializer


class RaceListView(generics.ListAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceListSerializer
    permission_classes = (AllowAny,)
