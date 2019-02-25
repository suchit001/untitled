from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'is_active','email', 'name', 'gender', 'birth_date','blood_group','emergency_contact_name', 'emergency_contact_number','address']
    list_editable =['is_active']


admin.site.register(CustomUser, admin_class=CustomUserAdmin)

admin.site.site_header="Cateina Admin"
admin.site.site_title="Cateina Admin"