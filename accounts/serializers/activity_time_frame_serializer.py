from rest_framework import serializers
from accounts.models import ActivityTimeFrame


class TimeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityTimeFrame
        fields = ('id', 'activity_time_frame')
        read_only_fields = ('id', 'activity_time_frame')
