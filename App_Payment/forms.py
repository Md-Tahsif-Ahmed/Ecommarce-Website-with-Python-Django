from django import forms
from .models import BillingAddress  # Import the BillingAddress model from your models.py

class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingAddress  # Associate the form with the BillingAddress model
        fields = ['address', 'zipcode', 'city', 'country']  # Specify the fields you want in the form

