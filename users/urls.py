from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView

from users.apps import UsersConfig
from django.urls import path

from users.views import UserCreateView, email_verification, CustomLoginView

app_name = UsersConfig.name


urlpatterns = [
    path('login/', CustomLoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', UserCreateView.as_view(), name='registration'),
    path('email-confirm/<str:token>', email_verification, name='email-confirm'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
]
