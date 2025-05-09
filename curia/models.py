from django.db import models
from accounts.models import Legionary

# Create your models here.
# Does the curia need a parish? Yes? for specification
class Curia(models.Model):
    name = models.CharField(max_length=100)
    inaug_date = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=50, default="Nigeria")
    archdiocese = models.CharField(max_length=100)
    parish = models.CharField(max_length=100)
    iden = models.CharField(max_length=20)
    creator = models.ForeignKey(
                Legionary, 
                on_delete=models.CASCADE, 
                related_name="curiae_created"
            )
    managers = models.ManyToManyField(Legionary)
    management_requests = models.ManyToManyField(
                Legionary, 
                related_name="curiae_management_requests",
                blank=True
            )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + "_curia"

    class Meta: 
        verbose_name_plural = 'curiae'


class Announcement(models.Model):
    '''
    - deadline: date to stop broadcasting the announcement
    - hidden_by: the list of names of legionaries who have hidden the announcement
        and will no longer have it display on their home page
    - ack_by: the list of names of legionaries who have acknowledged the 
        announcement and will no longer have it among their notifications
        or home page
    - creator_name: name of curia 
    '''
    curia = models.ForeignKey(Curia, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)  
    title = models.CharField(max_length=100)
    content = models.TextField()
    creator_name = models.CharField(max_length=200, blank=False)
    image = models.URLField(blank=True, null=True)
    # image = models.ImageField(upload_to='images/curia/', blank=True, null=True)
    hidden_by = models.JSONField(default=list, blank=True) 
    acknowledged_by = models.JSONField(default=list, blank=True) 

    def __str__(self):
        return self.title[:20]

