from django.db import models
from meetings.models import Meeting
from praesidium.models import Praesidium
from reports.models import Report 

# Create your models here.
class Work(models.Model):
    type = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    details = models.JSONField(default=dict, null=True, blank=True)
    meeting = models.ForeignKey(
        Meeting, on_delete=models.CASCADE, related_name='works'
        )

    def __str__(self):
        return "Work_" + self.type + "_" + str(self.meeting)

class WorkList(models.Model):
    praesidium = models.ForeignKey(Praesidium, on_delete=models.CASCADE, related_name='work_list')
    details = models.JSONField(default=list, blank=True) 

    def __str__(self): 
        return "WorkList for " + self.praesidium.name

class WorkTypeOption(models.Model):
    name = models.CharField(max_length=50)
    metrics = models.JSONField(default=list, blank=True)

    def __str__(self): 
        return self.name + "_work_type"

class WorkSummary(models.Model):
    type = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    no_assigned = models.IntegerField(default=0)
    no_done = models.IntegerField(default=0)
    details = models.JSONField(default=dict, null=True, blank=True)
    report = models.ForeignKey(Report, on_delete=models.CASCADE, 
            related_name="work_summaries")

    def __str__(self): 
        title = f"{self.type} Summary for Report {self.report.report_number} of {self.report.praesidium.name}"
        return title 

    class Meta: 
        verbose_name_plural = 'work summaries'
