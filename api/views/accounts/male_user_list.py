from accounts.serializers import UserListSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from accounts.models import CustomUser
from decouple import config


class MaleUserListView(ListAPIView):
    serializer_class = UserListSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = CustomUser.objects.filter(gender_id=config('MALE_ID'))
        return queryset
