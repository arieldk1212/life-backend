from .models import CustomUser
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ('username', 'email', 'password')

  def create(self, validated_data):
    password = validated_data.pop('password')
    user = super().create(validated_data)
    user.set_password(password)
    user.save()
    return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer): 
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)
    token['email'] = user.email
    token['username'] = user.username
    
    return token


class CustomUserUpdatePasswordSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ('username', 'password')

  def update(self, instance, validated_data):
    instance.set_password(validated_data['password'])
    instance.save()
    return instance
    
    
class CustomUserUpdateEmailSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=100)

  class Meta:
    model = CustomUser
    fields = ('email',)

  def validate_email(self, value):
    email = CustomUser.objects.filter(email=value).exists()
    if email:
      raise serializers.ValidationError('Email already exists')
    return value

  def update(self, instance, validated_data):
    instance.email = validated_data['email']
    instance.save()
    return instance
        
class CustomUserUpdateUsernameSerializer(serializers.ModelSerializer):
  username = serializers.CharField(max_length=20)

  class Meta:
    model = CustomUser
    fields = ('username',)

  def validate_username(self, value):
    username = CustomUser.objects.filter(username=value).exists()
    if username:
      raise serializers.ValidationError('Username already exists')
    return value

  def update(self, instance, validated_data):
    instance.username = validated_data['username']
    instance.save()
    return instance

class CustomUserDestroySerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ('username', 'password')

  def validate_password(self, value):
    