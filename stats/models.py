from django.db import models
from django.contrib.auth.models import User


# stats 模块的数据模型
class TokenUsage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tokens = models.IntegerField(default=0)
