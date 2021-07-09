from django.db import models


class ActivityTimeFrame(models.Model):
    """ 主な活動時間 """

    activity_time_frame = models.CharField('活動時間帯', max_length=40)

    def __str__(self):
        return self.activity_time_frame
