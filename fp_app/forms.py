from django import forms
from .models import Palmer

class PalmerForm(forms.ModelForm):
    class Meta:
        model = Palmer
        fields = ('raw_image', )