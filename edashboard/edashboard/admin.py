from django.contrib import admin
from django.contrib import auth
from edashboard.models import UserProfile
from .models import Building, Sensor
from .models import *

admin.site.register(Building)
admin.site.register(Sensor)
admin.site.register(SensorType)
admin.site.register(Connection)


class MyModelAdmin(admin.ModelAdmin):
    class Media:
        css = {
             'all': ('static/admin/adminstyle.css',)
        }
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'description','permission')
    def user_info(self, obj):
        return obj.description
    def user_permis(self, obj):
        return obj.permission

admin.site.register(UserProfile, UserProfileAdmin)
