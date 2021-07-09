from rest_framework import serializers

from accounts.models import CustomUser


class UserListSerializer(serializers.ModelSerializer):
    """ 登録時に使う """
    class Meta:
        model = CustomUser
        fields = (
            'id', 'user_name', 'user_icon', 'state_id', 'race_id')
