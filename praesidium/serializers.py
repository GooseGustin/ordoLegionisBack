from rest_framework import serializers 
from .models import Praesidium, Reminder
from accounts.models import Legionary 
from curia.serializers import getIden

class PraesidiumSerializer(serializers.ModelSerializer):
    # remove iden from serializer
    class Meta: 
        model = Praesidium 
        fields = [
            'id', 'name', 'state', 'country', 'parish', 'curia', 
            'iden', 'address', 'meeting_time', 'inaug_date', 
            'spiritual_director', 'spiritual_director_app_date',
            'president', 'pres_app_date', 'vice_president', 
            'vp_app_date', 'secretary', 'sec_app_date', 
            'treasurer', 'tres_app_date', 'managers', 'members',
            'membership_requests', 'management_requests',
            'next_report_deadline', 
            'created_at', 'reports' # 'work_list', 
        ]
        read_only_fields = [
            'id', 'iden', 'created_at'
            ]

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user = request.user 
            legionary = Legionary.objects.get(user=user)
            validated_data['managers'] = []
            validated_data['managers'].extend([legionary])
            validated_data['members'] = []
            validated_data['members'].extend([legionary])
            validated_data['iden'] = getIden(validated_data['name']) # iden remains the same even though the praesidium or curia name is changd
        return super().create(validated_data)

# praesidium serializer for staff 

class ReminderSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Reminder 
        fields = [
            'id', 'praesidium', 'creator_name',
            'content', 'deadline', 'date',
            'hidden_by', 'acknowledged_by'
        ]
        read_only_fields = ['hidden_by', 'acknowledged_by', 'date']

    def create(self, validated_data):

        praesidiumObj = validated_data.pop('praesidium', None)
        validated_data['praesidium'] = praesidiumObj 
        validated_data['creator_name'] = praesidiumObj.name 

        validated_data['hidden_by'] = []
        validated_data['acknowledged_by'] = []
        return super().create(validated_data)


# class PraesidiumSearchSerializer(serializers.Serializer):
#     praesidium = PraesidiumSerializer()