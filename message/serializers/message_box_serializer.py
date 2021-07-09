from rest_framework import serializers
from message.models import MessageBox
from rest_framework.serializers import SerializerMethodField


class MessageBoxSerializer(serializers.ModelSerializer):
    """メッセージの詳細取得"""
    male = SerializerMethodField()
    female = SerializerMethodField()

    class Meta:
        model = MessageBox
        fields = ('male_id', 'male', 'female_id', 'female', 'message', 'did_read', 'created_date')
        read_only_fields = ('male_id', 'male', 'female_id', 'female', 'message', 'did_read', 'created_date')

    def get_male(self, obj):
        try:
            user = obj.male_id.user_name
            return user
        except:
            return None

    def get_female(self, obj):
        try:
            user = obj.female_id.user_name
            return user
        except:
            return None
