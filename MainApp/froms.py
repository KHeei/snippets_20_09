from django.forms import ModelForm
from MainApp.models import Snippet
from django.forms.widgets import TextInput

class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ['name', 'lang', 'code']
        widgets = {
            'name': TextInput(attrs={"class": "form-control form-control-lg", 'placeholder': 'Название сниппета'}),
        }
        labels = {
            'name': ''
        }
