from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
  list_display = ('username', 'email', 'is_staff', 'created_at')
  search_fields = ('username', 'email')
  list_filter = ('username', 'email')


admin.site.register(CustomUser, CustomUserAdmin)

