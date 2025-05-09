from django.db import models
from praesidium.models import Praesidium

# Create your models here.
class Meeting(models.Model):
    date = models.DateField()
    meeting_no = models.IntegerField()
    praesidium = models.ForeignKey(Praesidium, on_delete=models.CASCADE, related_name="meetings")
    no_present = models.IntegerField()
    officers_meeting_attendance = models.JSONField(default=list)
    officers_curia_attendance = models.JSONField(default=list, blank=True)
    # last_edited = models.DateTimeField(auto_now=True) # display last meeting worked on on home page 

    def __str__(self):
        return "Meeting " + str(self.meeting_no) + " of " + self.praesidium.name

class MeetingNotes(models.Model): 
    meeting = models.OneToOneField(Meeting, on_delete=models.CASCADE, related_name='notes')
    content = models.TextField(default='', null=True, blank=True)