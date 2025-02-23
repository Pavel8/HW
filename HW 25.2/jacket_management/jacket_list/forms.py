from django import forms
from .models import Jacket

class JacketForm(forms.ModelForm):
    class Meta:
        model = Jacket
        exclude = ['created_at', 'updated_at']