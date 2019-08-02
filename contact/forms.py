from django import forms
#bringing in the Contact model from models
from .models import Contact

#creating form to accept user information when contacting us
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email','subject', 'message']
 