from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from MainApp.models import Snippet


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ['name', 'lang', 'code', 'is_private']
        widgets = {
            'name': TextInput(attrs={"class": "form-control form-control-lg", 'placeholder': 'Название сниппета'}),
        }
        labels = {
            'name': ''
        }


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
