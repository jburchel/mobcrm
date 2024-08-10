from django import forms
from .models import Contact, Church, Prospect, NonProspectInd 

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'type','first_name', 'last_name', 'email', 'phone', 
            'street_address', 'city', 'state', 'zip_code', 
            'image', 'notes', 'date_last_updated'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # You can add custom widgets, labels, or help texts here
        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['notes'].widget = forms.Textarea(attrs={'rows': 5})
        self.fields['date_last_updated'].widget = forms.DateInput(attrs={'type': 'date'})

        # Add Bootstrap classes to all form fields
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            
class ChurchForm(forms.ModelForm):
    class Meta:
        model = Church
        fields = [           
            'church_name','virtuous', 'primary_contact_first_name', 'primary_contact_last_name','senior_pastor_first_name','senior_pastor_last_name',
            'denomination', 'congregation_size', 'year_founded','missions_pastor_first_name', 'missions_pastor_last_name',
            'website','color','church_pipeline', 'priority','assigned_to', 'source', 'referred_by','info_given', 'reason_closed','date_closed' 
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make sure all fields are not required
        for field in self.fields:
            self.fields[field].required = False

class ProspectForm(forms.ModelForm):
    class Meta:
        model = Prospect
        fields = [           
            'home_country', 'spouse_recruit', 'virtuous', 'marital_status',
            'color','individual_pipeline', 'priority',
            'assigned_to', 'source', 'referred_by', 'date_closed',
            'info_given', 'desired_service', 'reason_closed'
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False

class NonProspectIndForm(forms.ModelForm):
    class Meta:
        model = NonProspectInd
        fields = [
            'marital_status', 'assigned_to',          
        ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make all fields optional
        for field in self.fields:
            self.fields[field].required = False