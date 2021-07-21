from django import forms
from django.forms import fields
from .models import Idea

class IdeaForm(forms.ModelForm):
    class Meta:
        model=Idea
        fields = '__all__' 