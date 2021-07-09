from django.contrib import admin

from accounts.models import ActivityTimeFrame, CustomUser, Gender, Race, State

admin.site.register(ActivityTimeFrame)
admin.site.register(CustomUser)
admin.site.register(Gender)
admin.site.register(Race)
admin.site.register(State)
