from django import forms
from django.forms import fields
from .models import Tool

class ToolForm(forms.ModelForm):
    class Meta:
        model=Tool
        fields = '__all__' 