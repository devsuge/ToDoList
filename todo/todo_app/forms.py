from django import forms
from django.contrib.admin import widgets

from .models import *


class TaskForm(forms.ModelForm):

    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = task
        fields = ['title', 'text', 'in_date', 'out_date']

