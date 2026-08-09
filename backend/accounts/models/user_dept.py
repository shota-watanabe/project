from django.db import models
from .user import User
from .dept import Dept

class UserDept(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dept = models.ForeignKey(
        Dept, to_field="code", db_column="dept_code", on_delete=models.CASCADE
    )
    is_primary = models.BooleanField(default=False)  # 主所属フラグ
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "dept")
