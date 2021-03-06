from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import Account


class AccountAdmin(UserAdmin):
    list_display = ('id', 'email', 'username', 'last_login', 'date_joined', 'is_staff')
    search_fields = ('id', 'email', 'username',)
    readonly_fields = ('id', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
