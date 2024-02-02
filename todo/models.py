from django.contrib.auth.models import User
from django.db import models
import datetime
from django.conf import settings

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=30, default=None)
    description = models.CharField(max_length=200)
    created_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None
    )