from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from message.serializers import MessagePreviewSerializer
from message.models import MessageBox


class ListMessageBoxView(generics.ListAPIView):
    serializer_class = MessagePreviewSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = MessageBox.objects.filter(female_id=self.request.user).order_by('created_date')
        return queryset
