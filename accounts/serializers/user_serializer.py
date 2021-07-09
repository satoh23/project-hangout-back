from rest_framework import serializers

from accounts.models import CustomUser, State


class UserSerializer(serializers.ModelSerializer):
    """ 登録時に使う """
    class Meta:
        model = CustomUser
        fields = (
            'id', 'user_name', 'email', 'password', 'gender_id', 'state_id')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        state = State.objects.get(pk=3)
        user = CustomUser(user_name=validated_data['user_name'],
                          email=validated_data['email'],
                          gender_id=validated_data['gender_id'],
                          state_id=state)
        user.set_password(validated_data['password'])
        user.save()
        return user
