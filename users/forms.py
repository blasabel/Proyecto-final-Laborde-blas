from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = {k: "" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField()
    first_name = forms.CharField()
    imagen = forms.ImageField(label="Avatar", required=False)

    class Meta:
        model = User
        fields = [
            'email',
            'last_name',
            'first_name',
            'imagen',
        ]
        help_texts = {k:"" for k in fields}