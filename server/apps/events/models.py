from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class PersonalPhoto(models.Model):
  photo_belonging = models.ForeignKey(User, on_delete=models.CASCADE)
  attachment = models.FileField(null=True, blank=True)
  
