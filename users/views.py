import secrets

from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import PasswordResetView, LoginView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
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


def generate_random_password():
    password = (secrets.token_hex(8))
    new_password = make_password(password)
    # print(new_password)
    return 'new_password'


def send_password_reset_email(email, password):
    send_mail(
        subject="Новый пароль",
        message=f"Привет, вот твой новый пароль {password}",
        from_email=EMAIL_HOST_USER,
        recipient_list=[email]
    )


class PasswordResetView(PasswordResetView):
    form_class = PasswordResetForm
    template_name = "users/password_reset.html"
    success_url = reverse_lazy('users:password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = generate_random_password()
        user = authenticate(email=email, password=password)
        if user is not None:
            user.set_password(password)
            user.save()
            send_password_reset_email(email, password)
        return super().form_valid(form)


class CustomLoginView(LoginView):
    model = User
    template_name = 'users/login.html'  # путь к вашему шаблону логина
    redirect_authenticated_user = True  # перенаправление аутентифицированных пользователей






