from rest_framework import serializers
from accounts.models import CustomUser


class PointGetSerializer(serializers.ModelSerializer):
    """各ユーザーのポイント取得に使う"""
    class Meta:
        model = CustomUser
        fields = ('id', 'own_point', 'user_icon', 'user_name', 'user_profile')
        read_only_fields = ('id', 'own_point', 'user_icon', 'user_name', 'user_profile')
