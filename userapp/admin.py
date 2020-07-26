from django.contrib import admin

# Register your models here.
from userapp.models import User
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token

from django.utils.translation import ugettext_lazy as _


class AdminUserapp(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'active', 'admin')
    readonly_fields = ('password',)
    fieldsets = (
            (_("Personal info"), {
                'fields':(
                    'email', 'first_name', 'middle_name',\
                    'last_name', 'phone_number', 'image'
                    )
                }
            ),
            (_("Permission"), {'fields':('staff',)}),)


admin.site.register(User, AdminUserapp)

admin.site.unregister(Group)

admin.site.unregister(Token)
