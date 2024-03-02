from django.forms import Form
from django.forms.fields import EmailField, CharField


class RegisterForm(Form):
    username = CharField(required=True)
    email = EmailField(required=True)
    password = CharField(required=True)

    password_confirm = CharField(required=True)

    first_name = CharField(required=False)
    last_name = CharField(required=False)


class LoginForm(Form):
    username = CharField(required=True)
    email = EmailField(required=True)
    password = CharField(required=True)
