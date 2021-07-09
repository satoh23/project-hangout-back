from rest_framework import serializers
from message.models import MessageBox
from accounts.models import Gender
from decouple import config


class CreateMessageSerializer(serializers.ModelSerializer):
    """メッセージの投稿に使う"""

    class Meta:
        model = MessageBox
        fields = ('male_id', 'female_id', 'message', 'did_read')

    def create(self, validated_data):
        male = Gender.objects.get(pk=config('MALE_ID'))
        female = Gender.objects.get(pk=config('FEMALE_ID'))
        if validated_data['male_id'].gender_id == male:
            if validated_data['female_id'].gender_id == female:
                message = MessageBox(male_id=validated_data['male_id'],
                                     female_id=validated_data['female_id'],
                                     message=validated_data['message'],)
                message.save()
                return message
        message = MessageBox()
        return message
