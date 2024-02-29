from django.forms import Form
from django.forms.fields import EmailField, CharField


class UserForm(Form):
    username = CharField(required=True)
    email = EmailField(required=True)
    password = CharField(required=True)
