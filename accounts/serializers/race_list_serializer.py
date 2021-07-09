from rest_framework import serializers
from accounts.models import Race


class RaceListSerializer(serializers.ModelSerializer):
    """各ユーザーの詳細取得に使う"""
    class Meta:
        model = Race
        fields = ('id', 'race')
        read_only_fields = ('id', 'race')
