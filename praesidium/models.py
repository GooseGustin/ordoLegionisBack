from django.db import models
from curia.models import Curia
from accounts.models import Legionary

# Create your models here.
class Praesidium(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=50, default="Nigeria")
    parish = models.CharField(max_length=50)
    curia = models.ForeignKey(Curia, on_delete=models.CASCADE, related_name="associated_praesidia")
    iden = models.CharField(max_length=20)
    address = models.CharField(max_length=100, default='')
    meeting_time = models.CharField(max_length=100)
    inaug_date = models.DateField(null=True, blank=True) 
    spiritual_director = models.CharField(max_length=100)
    spiritual_director_app_date = models.DateField(null=True, blank=True)
    president = models.CharField(max_length=100)
    pres_app_date = models.DateField(null=True, blank=True)
    vice_president = models.CharField(max_length=100)
    vp_app_date = models.DateField(null=True, blank=True)
    secretary = models.CharField(max_length=100)
    sec_app_date = models.DateField(null=True, blank=True)
    treasurer = models.CharField(max_length=100)
    tres_app_date = models.DateField(null=True, blank=True)
    managers = models.ManyToManyField(
                Legionary, 
                related_name="praesidia_managed"
            )
    members = models.ManyToManyField(
                Legionary, 
                related_name="associated_praesidia"
            )
    membership_requests = models.ManyToManyField(
                Legionary, 
                related_name="praesidia_membership_requests", 
                blank=True,
                # null=True
            )
    management_requests = models.ManyToManyField(
                Legionary, 
                related_name="praesidia_management_requests", 
                blank=True, 
                # null=True
            )
    next_report_deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + '_praesidium'

    class Meta: 
        verbose_name_plural = 'praesidia'

class Reminder(models.Model):
    praesidium = models.ForeignKey(
        Praesidium, on_delete=models.CASCADE, related_name="reminders"
    )
    creator_name = models.CharField(max_length=200, blank=False)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
    hidden_by = models.JSONField(default=list, blank=True) 
    acknowledged_by = models.JSONField(default=list, blank=True) 

# Reminders will be deleted 1 month after their deadlines 
