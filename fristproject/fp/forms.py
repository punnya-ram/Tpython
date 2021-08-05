from .models import Task
from django import forms
class fpForm (forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']