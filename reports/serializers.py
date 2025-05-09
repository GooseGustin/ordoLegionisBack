from rest_framework import serializers 
from .models import (
    Achievement, FunctionAttendance, MembershipDetail, Report
)
from works.serializers import WorkSummarySerializer

class AchievementSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Achievement
        fields = [
            'id', 'no_recruited', 'no_baptized', 'no_confirmed', 
            'no_first_communicants', 'no_married', 'no_vocations',
            'no_converted', 'others'
        ]


class ReportSerializer(serializers.ModelSerializer):
    achievements = AchievementSerializer()

    class Meta: 
        model = Report 
        fields = [
            'id', 'praesidium', 'submission_date', 'last_submission_date', 
            'report_number', 'report_period', 'last_curia_visit_date', 
            'last_curia_visitors', 'officers_curia_attendance', 
            'no_curia_meetings_held','no_praesidium_meetings_held',
            'no_curia_meetings_held_previous', 'no_praesidium_meetings_held_previous',
            'officers_meeting_attendance', 'extension_plans', 
            'problems', 'remarks', 'no_meetings_expected', 
            'no_meetings_held', 'avg_attendance', 'poor_attendance_reason', 
            'membership_details', 'include_intermediate', 'include_empty_achievements',
            'achievements', 'function_attendances', 'work_total_and_average', 
            'patricians_start', 'patricians_end', 
            'work_summaries', 'financial_summary', 'audited', 'auditor_1', 'auditor_2',
            'previous_curia_attendance', 'previous_meeting_attendance', 
            'read_and_accepted', 'conclusion'
        ]
        read_only_fields = ['function_attendances', 'work_summaries', 'financial_summary']

        # In create method, pop financial_summary from validated_data

    def create(self, validated_data):
        print("In create method of report")
        # Extract nested data
        achievement_data = validated_data.pop('achievements')
        # Create achievements
        achievement = Achievement.objects.create(**achievement_data)

        # Create Report
        report = Report.objects.create(
            achievements=achievement, 
            **validated_data
        )
        return report
        
    def update(self, instance, validated_data):
        print("In update method of report")
        
        # Handle nested achievements update
        achievement_data = validated_data.pop('achievements', None)
        if achievement_data:
            AchievementSerializer().update(instance.achievements, achievement_data)

        return super().update(instance, validated_data)


class FunctionAttendanceSerializer(serializers.ModelSerializer):
    class Meta: 
        model = FunctionAttendance
        fields = [
            'id', 'name', 'date', 'current_year_attendance', 
            'previous_year_attendance', 
            'report'
        ]



class MembershipDetailsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = MembershipDetail
        fields = [
            'id', 'affiliated_praesidia', 
            'active_members', 'probationary_members', 
            'auxiliary_members', 'adjutorian_members',
            'praetorian_members'
        ]


class ReportPrepGetSerializer(serializers.Serializer):
    last_submission_date = serializers.DateField()
    report_number = serializers.IntegerField()
    officers_curia_attendance = serializers.DictField(
        child=serializers.FloatField()
    )
    officers_meeting_attendance = serializers.DictField(
        child=serializers.FloatField()
    )
    no_meetings_expected = serializers.IntegerField()
    no_meetings_held = serializers.IntegerField()
    no_curia_meetings_held = serializers.DictField(
        child=serializers.FloatField()
    )
    no_praesidium_meetings_held = serializers.DictField(
        child=serializers.FloatField()
    )
    no_curia_meetings_held_previous = serializers.DictField(
        child=serializers.FloatField()
    )
    no_praesidium_meetings_held_previous = serializers.DictField(
        child=serializers.FloatField()
    )
    avg_attendance = serializers.IntegerField()
    work_summaries = serializers.ListField()
    financial_summary = serializers.ListField()


