from django.contrib import admin
from edashboard.models import UserProfile
from .models import Building, Sensor

admin.site.register(Building)
admin.site.register(Sensor)
from .models import *

class MyModelAdmin(admin.ModelAdmin):
    class Media:
        css = {
             'all': ('static/admin/adminstyle.css',)
        }
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ()
    def user_info(self, obj):
        return obj.description
    def user_permis(self, obj):
        return obj.permission

admin.site.register(UserProfile, UserProfileA
