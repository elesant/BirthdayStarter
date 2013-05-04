from django.contrib import admin
from core.models import OBUser, Present
from django.contrib.sessions.models import Session


class OBUserAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': ('email', 'facebook_id', 'tz_offset', 'display_name')
        }),
        ('Status', {
            'classes': ('collapse',),
            'fields': ('is_active', 'is_staff', 'is_superuser', 'last_login')
        }),
        ('Groups & Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions')
        }),
    )
    list_display = ('email', 'is_staff', 'last_login')
    search_fields = ['email']
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'last_login')
    filter_horizontal = ['groups', 'user_permissions']


admin.site.register(OBUser, OBUserAdmin)
admin.site.register(Present)
admin.site.register(Session)
