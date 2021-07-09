from rest_framework import serializers
from accounts.models import CustomUser


class EmailGetSerializer(serializers.ModelSerializer):
    """各ユーザーの詳細取得に使う"""
    class Meta:
        model = CustomUser
        fields = ('email',)
        read_only_fields = ('email',)
