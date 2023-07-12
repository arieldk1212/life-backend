from django.db import models
from apps.users.models import CommonUser

class Notes(CommonUser):
  note_id = models.IntegerField()
  note_name = models.CharField(max_length=20)
  note_description = models.TextField(blank=True, null=True, max_length=150)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self): return self.note_name
  
  class Meta:
    ordering = ['created_at']
    verbose_name = 'Notes'
  
class Todo(CommonUser):
  todo_id = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  todo_name = models.CharField(max_length=30)
  todo_description = models.TextField(blank=True, null=True, max_length=120)
  is_done = models.BooleanField(default=False)
  
  def __str__(self): return self.todo_name
  
  class Meta: 
    ordering = ['is_done']
    verbose_name = 'Todo List'
  


  
