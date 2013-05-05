from django.contrib import admin
from core.models import User, Present, Birthday, BirthdayContribution
from django.contrib.sessions.models import Session


class BirthdayContributionInline(admin.StackedInline):
    model = BirthdayContribution
    extra = 0


class BirthdayAdmin(admin.ModelAdmin):
    inlines = [BirthdayContributionInline]
    list_display = ('facebook_id', 'birthday', 'amount_raised', 'amount_target', 'time_modified',)
    search_fields = ['facebook_id']
    list_filter = ('time_created', 'time_modified',)


class UserAdmin(admin.ModelAdmin):

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


admin.site.register(User, UserAdmin)
admin.site.register(Present)
admin.site.register(Birthday, BirthdayAdmin)
admin.site.register(BirthdayContribution)
admin.site.register(Session)
