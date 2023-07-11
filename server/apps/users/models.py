from django.db import models
from .utils.uuid import generate_id
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class CustomUserManager(BaseUserManager):
  def create_user(self, email, username=None, password=None):
    if not email:
      raise ValueError('user Must Have An Email Address!')
    if not username:
      raise ValueError('user Must Have A Username!')
    if not password:
      raise ValueError('Need a Password to Continue...')
    email = self.normalize_email(email)
    user = self.model(email=email)
    user.set_password(password)
    user.save()
    return user

  def create_superuser(self, email, username=None, password=None, **kwargs):
    if not email:
      raise ValueError('user Must Have A Username!')
    if not username:
      raise ValueError('user Must Have An Email Address!')
    if not password:
      raise ValueError('Need a Password to Continue...')
    user = self.create_user(email, password)
    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.save()
    return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
  user_id = models.CharField(primary_key=True, max_length=32, default=generate_id, editable=False)
  email = models.EmailField(max_length=100, unique=True)
  username = models.CharField(max_length=20)
  is_admin = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  objects = CustomUserManager()

  def __str__(self): return self.username + ' - ' + self.email

  class Meta:
    verbose_name = 'User'
    verbose_name_plural = 'Users'
    ordering = ['-is_superuser', '-is_staff']

