from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS=['username']

    def __str__(self):
        return self.email 


STATUS_OPTIONS = [
    ('manager', 'Manager'),
    ('non-manager', 'Non-Manager'),
]

class Legionary(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, choices=STATUS_OPTIONS, default='non-manager'
    )
    premium_status = models.BooleanField(default=False)
    premium_status_deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return "Legionary_" + self.user.username

    class Meta: 
        verbose_name_plural = 'legionaries'

class Alert(models.Model):
    legionary = models.ForeignKey(Legionary, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    ack = models.BooleanField(default=False)

# class BlackList(models.Model):
#     legionaries = models.ManyToManyField