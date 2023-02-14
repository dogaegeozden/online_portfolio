# LIBRARIES
from django import forms
# MODELS
from contact.models import Message

# FORM CLASSES

# Creating a form class called MessageForm to control how the data will be collected 
class MessageForm(forms.ModelForm):
    class Meta:
        # Setting the form's data model
        model = Message
        # Creating a list of fields
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_num',
            'message',
        ]

    # Creating the form fields.
    first_name = forms.CharField(max_length=250, label="First Name")# max max_length = required
    last_name = forms.CharField(max_length=250, required=False, label="Last Name")# max max_length = required
    email = forms.EmailField(max_length=350, label="E-mail")
    phone_num = forms.CharField(max_length=100, required=False, label="Phone Number")
    message = forms.CharField(max_length=7500, label="Message")
