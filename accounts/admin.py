from django.contrib import admin
from .models import CustomUser, Legionary
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

# @admin.register(CustomUser) 
class CustomAdminUser(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

admin.site.register(Legionary)

#######################################33
@admin.register(CustomUser) 
class CustomUserAdmin(UserAdmin): 
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser 
    list_display = [
        'email', 'username', 'first_name', 'last_name', 'is_staff'
    ]
    # fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {'fields': ('email',)}), 
    # )
    add_fieldsets = (
        (
            None, {
                "classes": ("wide",),
                # "fields": ("email",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )