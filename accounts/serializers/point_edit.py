from rest_framework import serializers
from accounts.models import CustomUser


class PointEditSerializer(serializers.ModelSerializer):
    """各ユーザーのポイント取得に使う"""
    female_id = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ('own_point', 'female_id')
        read_only_fields = ('own_point',)
