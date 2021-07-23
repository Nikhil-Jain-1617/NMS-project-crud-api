from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only =True, required=True,validators=[validate_password])
    confirm_password = serializers.CharField(write_only= True, required= True)
    email = serializers.EmailField(required= True,validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(required= True,validators=[UniqueValidator(queryset=User.objects.all())])


    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'confirm_password',     # these fields we have to declared in models.py if not then declare it above like we did confirm_passowrd .
            'phone_no'
        )
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Password field didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            phone_no = validated_data['phone_no'],
            
        )

        user.set_password(validated_data['password'])    # for encrypting the raw password into hashing we used "set_password".
        user.save()

        return user
