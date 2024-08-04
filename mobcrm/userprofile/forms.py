from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    organization_name = forms.CharField(max_length=100)
    role = forms.ChoiceField(choices=[
        ('Base Mobilizer', 'Base Mobilizer'),
        ('Regional Mobilizer', 'Regional Mobilizer'),
        ('Goblal Team', 'Global Team'),
        ('Mobilization Director', 'Mobilization Director'),
        ('Office Executive Director', 'Office Executive Director'),
        ('Other', 'Other'),
    ])

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['role']  # Add any other fields you want users to be able to edit
    
