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
        self.fields['notes'].widget = forms.Textarea(attrs={'rows': 3})
        self.fields['date_last_updated'].widget = forms.DateInput(attrs={'type': 'date'})

        # Add Bootstrap classes to all form fields
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            
class ChurchForm(forms.ModelForm):
    church_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    street_address = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=50)
    zipcode = forms.CharField(max_length=10)
    image = forms.ImageField(required=False)
    notes = forms.CharField(widget=forms.Textarea, required=False)
    type = forms.CharField(max_length=20)
    last_contacted = forms.DateField(required=False)

    class Meta:
        model = Church
        fields = [
            # Fields from Contact model
            'church_name', 'email', 'phone', 'street_address', 'city', 'state', 
            'zipcode', 'image', 'notes', 'type', 'last_contacted',
            
            # Fields specific to Church model
            'website', 'denomination', 'congregation_size', 'senior_pastor_first_name','senior_pastor_last_name',
            'missions_pastor_first_name', 'missions_pastor_last_name',
            'color','church_pipeline', 'priority',
            'assigned_to', 'source', 'referred_by', 'virtuous', 'date_closed',
            'info_given', 'reason_closed'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If we're editing an existing Church, populate the Contact fields
        if self.instance.pk:
            contact = self.instance.contact_ptr
            for field in self.fields:
                if hasattr(contact, field):
                    self.fields[field].initial = getattr(contact, field)

    def save(self, commit=True):
        church = super().save(commit=False)
        # Update the Contact fields
        contact = church.contact_ptr
        for field in self.cleaned_data:
            if hasattr(contact, field):
                setattr(contact, field, self.cleaned_data[field])
        if commit:
            contact.save()
            church.save()
        return church

class ProspectForm(forms.ModelForm):
    # Explicitly declare fields from Contact model
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    street_address = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=50)
    zipcode = forms.CharField(max_length=10)
    image = forms.ImageField(required=False)
    notes = forms.CharField(widget=forms.Textarea, required=False)
    type = forms.CharField(max_length=20)
    last_contacted = forms.DateField(required=False)

    class Meta:
        model = Prospect
        fields = [
            # Fields from Contact model
            'first_name', 'last_name', 'email', 'phone', 'street_address',
            'city', 'state', 'zipcode', 'image', 'notes', 'type', 'last_contacted',
            
            # Fields specific to Prospect model
            'home_country', 'spouse_recruit', 'virtuous', 'marital_status',
            'color','individual_pipeline', 'priority',
            'assigned_to', 'source', 'referred_by', 'date_closed',
            'info_given', 'desired_service', 'reason_closed'
        ]

class NonProspectIndForm(forms.ModelForm):
    # Explicitly declare fields from Contact model
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    street_address = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=50)
    zipcode = forms.CharField(max_length=10)
    image = forms.ImageField(required=False)
    notes = forms.CharField(widget=forms.Textarea, required=False)
    type = forms.CharField(max_length=20)
    last_contacted = forms.DateField(required=False)

    class Meta:
        model = NonProspectInd
        fields = [
            # Fields from Contact model
            'first_name', 'last_name', 'email', 'phone', 'street_address',
            'city', 'state', 'zipcode', 'image', 'notes', 'type', 'last_contacted',
            
            # Fields specific to NonProspectInd model
            'marital_status', 'assigned_to',
            # Add any other fields specific to NonProspectInd
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If we're editing an existing NonProspectInd, populate the Contact fields
        if self.instance.pk:
            contact = self.instance.contact_ptr
            for field in self.fields:
                if hasattr(contact, field):
                    self.fields[field].initial = getattr(contact, field)

    def save(self, commit=True):
        non_prospect = super().save(commit=False)
        # Update the Contact fields
        contact = non_prospect.contact_ptr
        for field in self.cleaned_data:
            if hasattr(contact, field):
                setattr(contact, field, self.cleaned_data[field])
        if commit:
            contact.save()
            non_prospect.save()
        return non_prospect