from rest_framework import serializers

from accounts.models import CustomUser
from rest_framework.serializers import SerializerMethodField


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


class UserEditSerializer(serializers.ModelSerializer):
    """ 編集時に使う """
    user_icon = Base64ImageField(max_length=None, use_url=True)
    race = SerializerMethodField()
    activity_time_frame = SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = (
            'id', 'user_name', 'email', 'password',
            'user_profile', 'user_icon', 'encoded_icon', 'user_twitter_url',
            'gender_id', 'state_id', 'activity_time_frame_id', 'activity_time_frame', 'race_id', 'race')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
        read_only_fields = ('id', 'email', 'gender_id', 'activity_time_frame', 'race')

    def get_activity_time_frame(self, obj):
        try:
            time_frame = obj.activity_time_frame_id.activity_time_frame
            return time_frame
        except:
            return None

    def get_race(self, obj):
        try:
            race = obj.race_id.race
            return race
        except:
            return None
