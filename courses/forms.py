from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False, label="Email (ixtiyoriy)")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        labels = {
            'username': "Foydalanuvchi nomi",
            'password1': "Parol",
            'password2': "Parolni tasdiqlang",
        }
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            if field_name in labels:
                field.label = labels[field_name]
