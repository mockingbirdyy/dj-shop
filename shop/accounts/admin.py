from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from .models import User
from .forms import UserChangeForm, UserCreationForm


class UserAdmin(UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('full_name', 'email', 'phone_number')
    fieldsets = (
        ("UserInfo",
            {"fields": ('full_name', 'email', 'phone_number', 'password')}),

        ("permisions",
            {'fields': ('is_admin', 'is_active', 'last_login')})
    )

    add_fieldsets = (
        ("UserInfo",
            {"fields": ('full_name', 'email', 'phone_number', 'password1', 'password2')}),

    )
    list_filter = ('is_admin',)
    ordering = ('full_name',)
    search_fields = ('phone_number', 'full_name')
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
