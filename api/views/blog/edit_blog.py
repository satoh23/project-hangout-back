from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from blog.serializers import BlogDetailSerializer
from blog.models import BlogDetail
from django.http.response import JsonResponse


class EditBlogView(generics.RetrieveUpdateAPIView):
    queryset = BlogDetail.objects.all()
    serializer_class = BlogDetailSerializer
    permission_classes = (IsAuthenticated,)

    def patch(self, request, *args, **kwargs):
        try:
            user_id = request.COOKIES['UID']
            if user_id == request.data['author_id']:
                return self.partial_update(request, *args, **kwargs)
            return JsonResponse({'status': 'false', 'message': 'このユーザーは記事の編集ができません'},
                                status=401)
        except KeyError:
            pass
        return JsonResponse({'status': 'false', 'message': 'このユーザーは記事の編集ができません'},
                            status=401)
