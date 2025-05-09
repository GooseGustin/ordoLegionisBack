from django.db import models
from praesidium.models import Praesidium

# Create your models here.

class MembershipDetail(models.Model):
    affiliated_praesidia = models.JSONField(default=list) # senior, intermediate, junior
    active_members = models.JSONField(default=list)
    probationary_members = models.JSONField(default=list)
    auxiliary_members = models.JSONField(default=list)
    adjutorian_members = models.JSONField(default=list)
    praetorian_members = models.JSONField(default=list)

class Achievement(models.Model):
    no_recruited = models.JSONField(default=list)
    no_baptized = models.JSONField(default=list)
    no_confirmed = models.JSONField(default=list)
    no_first_communicants = models.JSONField(default=list)
    no_married = models.JSONField(default=list)
    no_vocations = models.JSONField(default=list)
    no_converted = models.JSONField(default=list)
    others = models.JSONField(default=dict, null=True, blank=True)

class Report(models.Model):
    # A manager can create a report for whatever time range they specify for that praesidium
    praesidium = models.ForeignKey(Praesidium, on_delete=models.CASCADE, related_name='reports')
    submission_date = models.DateField(null=True, blank=True)
    last_submission_date = models.DateField(null=True, blank=True)
    report_number = models.IntegerField(default=0)
    report_period = models.IntegerField(default=0) # days
    last_curia_visit_date = models.DateField(null=True, blank=True)
    last_curia_visitors = models.TextField(null=True, blank=True)
    officers_curia_attendance = models.JSONField(default=dict)
    officers_meeting_attendance = models.JSONField(default=dict)

    previous_curia_attendance = models.JSONField(default=dict)
    previous_meeting_attendance = models.JSONField(default=dict)

    no_curia_meetings_held = models.JSONField(default=dict)
    no_praesidium_meetings_held = models.JSONField(default=dict)
    no_curia_meetings_held_previous = models.JSONField(default=dict)
    no_praesidium_meetings_held_previous = models.JSONField(default=dict)

    extension_plans = models.TextField(null=True, blank=True)
    problems = models.TextField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    no_meetings_expected = models.IntegerField(default=0)
    no_meetings_held = models.IntegerField(default=0)
    avg_attendance = models.IntegerField(default=0)
    poor_attendance_reason = models.TextField(null=True, blank=True)
    membership_details = models.OneToOneField(MembershipDetail, on_delete=models.CASCADE)
    achievements = models.OneToOneField(Achievement, on_delete=models.CASCADE)
    work_total_and_average = models.JSONField(default=dict)

    include_intermediate = models.BooleanField(default=True)
    include_empty_achievements = models.BooleanField(default=True)
    patricians_start = models.CharField(max_length=8, default='Jan 2024', null=True, blank=True) 
    patricians_end = models.CharField(max_length=8, default='Dec 2024', null=True, blank=True)
    audited = models.BooleanField(default=False)
    auditor_1 = models.CharField(max_length=100, default='', blank=True)
    auditor_2 = models.CharField(max_length=100, default='', blank=True)
    read_and_accepted = models.BooleanField(default=True)
    conclusion = models.TextField(default='This report was carefully extracted from the records of the praesidium, which include the worksheet, roll call book, minutes book, and treasurer\'s book.')


    def __str__(self):
        return "Report " + str(self.report_number) + " of " + self.praesidium.name

class FunctionAttendance(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(null=True, blank=True)
    current_year_attendance = models.IntegerField(default=0)
    previous_year_attendance = models.IntegerField(default=0)
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name="function_attendances")

    def __str__(self): 
        string = self.name + " for report " + str(self.report.report_number) + " of " + self.report.praesidium.name
        return string 