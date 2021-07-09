from rest_framework import serializers
from accounts.models import CustomUser


class UserDetailSerializer(serializers.ModelSerializer):
    """各ユーザーの詳細取得に使う"""
    class Meta:
        model = CustomUser
        fields = ('id', 'user_name', 'user_profile', 'user_icon', 'user_twitter_url',
                  'state_id', 'activity_time_frame_id', 'race_id', 'gender_id')
        read_only_fields = ('id', 'user_name', 'user_profile', 'user_icon', 'user_twitter_url',
                            'state_id', 'activity_time_frame_id', 'race_id', 'gender_id')

