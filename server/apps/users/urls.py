from .views import *
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
  path('sign-up/', SignupView.as_view(), name='sign_up'),
  path('login/', MyTokenObtainPairView.as_view(), name='login'),
  path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('update-email/', UpdateUserEmailView.as_view(), name='update_email'),
  path('update-username/', UpdateUserUsernameView.as_view(), name='update_username'),
  path('reset-password/', ChangePasswordView.as_view(), name='reset_password'),
  path('delete-account/', DestroyUserView.as_view(), name='delete_account')
]