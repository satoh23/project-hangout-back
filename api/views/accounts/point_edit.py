from accounts.serializers import PointEditSerializer
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.models.custom_user import CustomUser


class PointEditView(RetrieveUpdateAPIView):
    """
    cookieにAccessTokenが入っている時だけアクセス可能
    """
    serializer_class = PointEditSerializer
    permission_classes = (IsAuthenticated,)
    queryset = CustomUser.objects.all()

    def get_object(self):
        return self.request.user

    def patch(self, request, *args, **kwargs):
        male_user = self.request.user
        female_user = CustomUser.objects.get(pk=request.data['female_id'])
        male_user.own_point -= 0
        female_user.own_point += 0
        male_user.save()
        female_user.save()
        return self.partial_update(request, *args, **kwargs)
