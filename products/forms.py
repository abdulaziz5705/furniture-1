from .models import ColourModel
from django import forms


class ColorAdminForm(forms.ModelForm):
    class Meta:
        model = ColourModel
        fields = ['code' , 'name']
        widgets = {
            'code': forms.TextInput(attrs={'type': 'color'})
        }
