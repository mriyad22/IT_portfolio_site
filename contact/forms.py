from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    # A honeypot field can catch simple bots; it is hidden in the template.
    website = forms.CharField(required=False, widget=forms.HiddenInput, label="Leave this field empty")

    class Meta:
        model = ContactMessageModel
        fields = ["name", "email", "phone", "company", "service", "subject", "message"]
        
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your full name", "autocomplete": "name", "maxlength": "100"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "you@company.com", "autocomplete": "email"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "+880...", "autocomplete": "tel", "maxlength": "30"}),
            "company": forms.TextInput(attrs={"class": "form-control", "placeholder": "Company (optional)", "maxlength": "120"}),
            "service": forms.Select(attrs={"class": "form-select"}),
            "subject": forms.TextInput(attrs={"class": "form-control", "placeholder": "How can we help?", "maxlength": "160"}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Tell us a little about your project...", "maxlength": "5000"}),
        }

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if len(name) < 2:
            raise forms.ValidationError("Please enter at least 2 characters.")
        return name

    def clean_subject(self):
        subject = self.cleaned_data["subject"].strip()
        if len(subject) < 4:
            raise forms.ValidationError("Subject must contain at least 4 characters.")
        return subject

    def clean_message(self):
        message = self.cleaned_data["message"].strip()
        if len(message) < 20:
            raise forms.ValidationError("Please provide at least 20 characters so we can understand your request.")
        return message
