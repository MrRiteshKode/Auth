from django import forms
from .models import About

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ("fullName","about")
        widgets = {
            'fullName':forms.TextInput(attrs={'class':'form-control mb-2'}),
            'about':forms.Textarea(attrs={'rows':6,'class':'form-control mb-2'}),
            # 'user':forms.TextInput(attrs={'class':'form-control mb-2 visually-hidden'}),
        }