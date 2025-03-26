from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleModel
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, 
                                     required=True,
                                     allow_blank=False)
    status = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = UserModel
        exclude = ('is_staff','is_superuser','last_login')
        extra_kwargs = {
            'status': {'required': False}
            }
    
    def save(self):
        instance = self.instance
        validated_data = self.validated_data

        if instance:
            instance.email = self.validated_data.get('email', instance.email)
            instance.name = self.validated_data.get('name', instance.name)
            instance.role = self.validated_data.get('role', instance.role)

            if 'password' in self.validated_data:
                instance.set_password(self.validated_data['password'])
            instance.save()
            return instance
        else:
            user= UserModel(**validated_data)
            user.set_password(validated_data['password'])
            user.save()

class LoginSerializer(serializers.Serializer):
    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            'password': attrs['password']
        }

        user=authenticate(**authenticate_kwargs)

        if user and user.status:
            return super().validate(attrs)
        
        raise serializers.ValidationError('Invalid credentials')

    @classmethod  
    def get_token(self,user):
        token = super().get_token(user)
        token['name'] = user.name
        token['email'] = user.email
        token['role'] = user.role.name
        return token
        

