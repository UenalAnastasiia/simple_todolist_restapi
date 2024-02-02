from django.contrib.auth.models import User
from django.db import models
import datetime
from datetime import date

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
    
    
    # def get_user_name(self):
    #     """
    #     return user data
    #     """
    #     return self.user.first_name
    
    
    def time_passed(self):
        """
        return days since todo was created
        """
        today = date.today()
        delta = today - self.created_at
        return delta.days