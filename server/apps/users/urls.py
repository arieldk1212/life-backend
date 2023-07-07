from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import SignupView, MyTokenObtainPairView, ChangePasswordView, UpdateUserEmailView, UpdateUserUsernameView


urlpatterns = [
  path('sign-up/', SignupView.as_view(), name='sign_up'),
  path('login/', MyTokenObtainPairView.as_view(), name='login'),
  path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('update-email/', UpdateUserEmailView.as_view(), name='update_email'),
  path('update-username/', UpdateUserUsernameView.as_view(), name='update_username'),
  path('reset-password/', ChangePasswordView.as_view(), name='reset_password'),
  # path('logout/', ChangePasswordView.as_view(), name='reset_password'),
  # path('delete-account/', ChangePasswordView.as_view(), name='reset_password'),
]