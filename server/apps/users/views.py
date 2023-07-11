from .serializers import  *
from api.permissions import *
from .models import CustomUser
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

class SignupView(APIView):
  # permission_classes = [AllowAnyPermission]

  def post(self, request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer

class CustomUserListView(generics.ListAPIView):
  permission_classes = [AdminUserPermission]
  serializer_class = CustomUserListSerializer
  queryset = CustomUser.objects.all()
  
  def get_queryset(self):
    user = self.request.user
    if user.is_superuser:
      return CustomUser.objects.all()
    return CustomUser.objects.filter(username=user.username)
    
class ChangePasswordView(generics.UpdateAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = CustomUserUpdatePasswordSerializer

  def get_object(self, queryset=None):
    return self.request.user

  def update(self, request, *args, **kwargs):
    self.object = self.get_object()
    serializer = self.get_serializer(data=request.data)
    if serializer.is_valid():
      self.object.set_password(serializer.data.get('password'))
      self.object.save()
      response={
        'status': status.HTTP_200_OK,
        'message': 'Password changed successfully',
        'data': []
      }
      return Response(response)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserEmailView(generics.UpdateAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = CustomUserUpdateEmailSerializer

  def get_object(self, queryset=None):
    return self.request.user

  def update(self, request, *args, **kwargs):
    self.object = self.get_object()
    serializer = self.get_serializer(data=request.data)
    if serializer.is_valid():
      self.object.email = serializer.data.get('email')
      self.object.save()
      response={
       'status': status.HTTP_200_OK,
       'message': 'Profile updated successfully',
        'data': []
      }
      return Response(response)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UpdateUserUsernameView(generics.UpdateAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = CustomUserUpdateUsernameSerializer

  def get_object(self, queryset=None):
    return self.request.user

  def update(self, request, *args, **kwargs):
    self.object = self.get_object()
    serializer = self.get_serializer(data=request.data)
    if serializer.is_valid():
      self.object.username = serializer.data.get('username')
      self.object.save()
      response={
       'status': status.HTTP_200_OK,
       'message': 'Profile updated successfully',
        'data': []
      }
      return Response(response)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DestroyUserView(generics.DestroyAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = CustomUserDestroySerializer

  def get_object(self, queryset=None):
    return self.request.user
  
  def destroy(self, request, *args, **kwargs):
    self.object = self.get_object()
    self.object.delete()
    response={
     'status': status.HTTP_200_OK,
     'message': 'User deleted successfully',
      'data': []
    }
    return Response(response)