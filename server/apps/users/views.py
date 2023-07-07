from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomUserSerializer, MyTokenObtainPairSerializer, CustomUserUpdatePasswordSerializer, CustomUserUpdateEmailSerializer, CustomUserUpdateUsernameSerializer


class SignupView(APIView):
  def post(self, request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer


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