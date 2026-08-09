from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Dept, Role, UserDept, UserRole

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = list(BaseUserAdmin.fieldsets or []) + [
        ("業務情報", {"fields": ("full_name",)}),
    ]

admin.site.register(Dept)
admin.site.register(Role)
admin.site.register(UserDept)
admin.site.register(UserRole)
