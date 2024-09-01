import secrets

from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import PasswordResetView, LoginView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from catalog.forms import StyleFormMixin
from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView, StyleFormMixin):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            subject="Подтверждение почты",
            message=f"Привет, для подтверждения почты необходимо перейти по этой ссылке {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))



class PasswordResetView(PasswordResetView, StyleFormMixin):
    form_class = PasswordResetForm
    template_name = "users/password_reset.html"
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = User.objects.get(email=email)
        password = User.objects.make_random_password(length=10)
        if user is not None:
            send_mail(
                subject="Новый пароль",
                message=f"Привет, вот твой новый пароль {password}",
                from_email=EMAIL_HOST_USER,
                recipient_list=[email]
            )
            user.set_password(password)
            user.save()
        return redirect(reverse('users:login'))



class CustomLoginView(LoginView):
    model = User
    template_name = 'users/login.html'  # путь к вашему шаблону логина
    redirect_authenticated_user = True  # перенаправление аутентифицированных пользователей






