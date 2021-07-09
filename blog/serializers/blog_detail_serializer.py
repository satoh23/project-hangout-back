from rest_framework import serializers
from blog.models import BlogDetail
from accounts.models import Gender
from decouple import config


class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        if isinstance(data, six.string_types):
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            file_name = str(uuid.uuid4())[:12]
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = "%s.%s" % (file_name, file_extension, )
            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class BlogDetailSerializer(serializers.ModelSerializer):
    """ブログの作成、編集に使う"""

    thumbnail = Base64ImageField(max_length=None, use_url=True)

    class Meta:
        model = BlogDetail
        fields = ('thumbnail', 'encoded_thumbnail', 'title', 'summary', 'body', 'price', 'author_id', 'genre_id')

    def create(self, validated_data):
        female = Gender.objects.get(pk=config('FEMALE_ID'))
        if validated_data['author_id'].gender_id == female:
            blog = BlogDetail(thumbnail=validated_data['thumbnail'],
                              encoded_thumbnail=validated_data['encoded_thumbnail'],
                              title=validated_data['title'],
                              body=validated_data['body'],
                              price=validated_data['price'],
                              author_id=validated_data['author_id'],
                              genre_id=validated_data['genre_id'],
                              )
            blog.save()
            return blog
        blog = BlogDetail()
        return blog
