from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from .models import User, OtpCode
from .forms import UserChangeForm, UserCreationForm

@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code', 'created')

class UserAdminClass(UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('full_name', 'email', 'phone_number')
    fieldsets = (
        ("UserInfo",
            {"fields": ('full_name', 'email', 'phone_number', 'password')}),

        ("permissions",
            {'fields': ('is_admin', 'is_active', 'is_superuser', 'last_login', 'groups', 'user_permissions')})
    )

    add_fieldsets = (
        ("UserInfo",
            {"fields": ('full_name', 'email', 'phone_number', 'password1', 'password2')}),

    )
    list_filter = ('is_admin',)
    ordering = ('full_name',)
    search_fields = ('phone_number', 'full_name')
    filter_horizontal = ('groups', 'user_permissions')



admin.site.register(User, UserAdminClass)
