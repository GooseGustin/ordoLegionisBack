from rest_framework import serializers
from .models import Announcement, Curia
from accounts.models import Legionary 
from random import randint, shuffle

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Announcement
        fields = [
            'id', 'curia', 'date', 
            'deadline', 'title', 'creator_name', 
            'content', 'image', 
            'hidden_by', 'acknowledged_by'
        ]
        read_only_fields = ['date', 'hidden_by', 'acknowledged_by']

    def create(self, validated_data):

        curiaObj = validated_data.pop('curia', None)
        validated_data['curia'] = curiaObj
        validated_data['creator_name'] = curiaObj.name 

        # print("In announcement serializer, image", validated_data.image)

        validated_data['hidden_by'] = []
        validated_data['acknowledged_by'] = []
        return super().create(validated_data)

    def edit(self, validated_data):
    
        curiaObj = validated_data.pop('curia', None)
        validated_data['curia'] = curiaObj
        validated_data['creator_name'] = curiaObj.name 

        return super().edit(validated_data)

    
def getIden(name):
    letters = [i[0] for i in name.split(' ')]
    pepper = [str(randint(0,50)) for _ in range(3)]
    letters.extend(pepper) 
    shuffle(letters)
    letters = ''.join(letters)
    return letters

class CuriaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Curia
        fields = [
            'id', 'name', 'iden', 'inaug_date', 'email',
            'state', 'country', 'archdiocese', 'parish',
            'creator', 'created_at',
            'managers', 'management_requests'
        ]
        read_only_fields = ['creator', 'created_at', 'iden']  

    def create(self, validated_data):
        request = self.context.get('request')

        if request and hasattr(request, 'user'):
            user = request.user 
            legionary = Legionary.objects.get(user=user)
            validated_data['creator'] = legionary 
            # validated_data['managers'] = []
            # validated_data['managers'].extend([legionary])
            validated_data['iden'] = getIden(validated_data['name'])
        return super().create(validated_data)



# class CuriaSearchSerializer(serializers.Serializer):
#     curia = CuriaSerializer()