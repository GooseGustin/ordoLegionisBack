from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Feedback(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="feedback")
    content = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)