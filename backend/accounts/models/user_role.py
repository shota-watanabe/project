from django.db import models
from .user import User
from .role import Role

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(
        Role, to_field="code", db_column="role_code", on_delete=models.CASCADE
    )
    granted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "role")
