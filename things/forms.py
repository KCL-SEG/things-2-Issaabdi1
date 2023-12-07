"""Forms of the project."""
from .models import Thing
from django import forms

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        exclude = ['created_at']
        widgets = {
            'description': forms.Textarea(),
            'quantity': forms.NumberInput(),
        }

