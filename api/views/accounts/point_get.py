from accounts.serializers import PointGetSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.models.custom_user import CustomUser


class PointGetView(RetrieveAPIView):
    """
    cookieにAccessTokenが入っている時だけアクセス可能
    """
    serializer_class = PointGetSerializer
    permission_classes = (IsAuthenticated,)
    queryset = CustomUser.objects.all()

    def get_object(self):
        return self.request.user
