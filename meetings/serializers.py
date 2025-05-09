from rest_framework import serializers
from .models import Meeting, MeetingNotes


class MeetingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Meeting
        fields = [
            'id', 
            'date', 
            'praesidium', 
            'meeting_no',
            'no_present', 
            'officers_meeting_attendance',
            'officers_curia_attendance', 
            'notes'
        ]
        read_only_fields = ['notes']


class MeetingNotesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = MeetingNotes
        fields = [
            'id', 
            'meeting', 
            'content'
        ]
