from django import forms
from .models import Author


class AuthorForms(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'email', 'biography', 'birthday']
