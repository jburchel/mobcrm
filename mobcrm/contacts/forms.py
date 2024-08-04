from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name','type', 'email', 'phone', 'last_contact']
        widgets = {
            'last_contact': forms.DateInput(attrs={'type': 'date'}),
        }