from .models import Alert, CustomUser, Legionary
# from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
from rest_framework import serializers 

class CustomUserSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_authenticated'] 
    
class UserRegistrationSerializer(serializers.ModelSerializer): 
    password1 = serializers.CharField(write_only=True) 
    password2 = serializers.CharField(write_only=True) 

    class Meta: 
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'password1', 'password2'
        ]
        extra_kwargs = {'password': {
            'write_only': True
        }}

    def validate(self, attrs): 
        if attrs['password1'] != attrs['password2']: 
            raise serializers.ValidationError('Passwords do not match!')

        password = attrs.get('password1', "")
        if len(password) < 8: 
            raise serializers.ValidationError("Passwords must be at least 8 characters!") 

        return attrs 

    def create(self, validated_data): 
        password = validated_data.pop('password1') 
        validated_data.pop('password2') 

        user = CustomUser.objects.create_user(password=password, **validated_data)  # type: ignore
        # Add new user to default basic group 
        # Basic_Group, _ = Group.objects.get_or_create(name='Basic_Group')
        # user.groups.add(Basic_Group)
        # user.save()
        # Create new legionary
        Legionary.objects.create(user=user) # , **validated_data)
        return user 

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True) 

    def validate(self, data): 
        print("In login validate method", data)
        user = authenticate(**data) 
        print("user", user)
        if user and user.is_active: 
            return user 
        else: 
            raise serializers.ValidationError("Incorrect credentials")

class LegionarySerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta: 
        model = Legionary        
        fields = [
            'id',
            'user', 
            'status', 
        ]
