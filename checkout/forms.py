from django import forms
from .models import Order


# Delivery details form
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name',
            'email',
            'phone_number',
            'street_address1',
            'street_address2',
            'town_or_city',
            'postcode',
            'country',
            'county',)

    def __init__(self, *args, **kwargs):
        """
        Adds placeholders and classes to form fields,
        removes auto-generated labels
        """
        super().__init__(*args, **kwargs)
        # Sets placeholders in each form field
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'county': 'County or State',
            'postcode': 'Postal Code',
            'phone_number': 'Phone Number',
        }

        # Sets autofocus to first field
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            # Checks if empty field is not country
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
