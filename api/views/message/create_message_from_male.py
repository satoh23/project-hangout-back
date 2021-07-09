from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from message.serializers import CreateMessageSerializer
from message.models import MessageBox
from accounts.models import CustomUser
from rest_framework.response import Response
from rest_framework import status


class CreateMessageFromMaleView(generics.CreateAPIView):
    queryset = MessageBox.objects.all()
    serializer_class = CreateMessageSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            male = self.request.user
            female = CustomUser.objects.get(pk=request.data['female_id'])
            if male.own_point < 10:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'ポイントが足りませんでした'})
            male.own_point -= 10
            female.own_point += 5
            male.save()
            female.save()
            return self.create(request, *args, **kwargs)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'メッセージを送信できませんでした'})
