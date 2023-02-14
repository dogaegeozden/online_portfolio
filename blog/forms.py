# LIBRARIES
from django import forms
# MODELS
from blog.models import Subscription, Comment

# FORM CLASSES

# Creating a class called SubscriptionForm to control how the data will be collected 
class SubscriptionForm(forms.ModelForm):
    
    # Creating a class called Meta to set the data model that will be used in this form and the fields.
    class Meta:
    
        # Setting the model to Subscription data model.
        model = Subscription

        # Setting the fields list.
        fields = [
            'email',
        ]

    # Creating the form's fields.
    email = forms.EmailField(max_length=350, label="E-mail")


# Creating a class called CommentForm to control how the data will be collected 
class CommentForm(forms.ModelForm):
    
    # Creating a class called Meta to set the data model that will be used in this form and the fields.
    class Meta:

        # Setting the model to Comment data model.
        model = Comment

        # Setting the fields list.
        fields = [
            'name',
            'text',
        ]

    # Creating the form's fields
    name = forms.CharField(max_length=150, label="Name")# max max_length = required
    text = forms.CharField(max_length=1500, label="Body", widget=forms.Textarea(attrs={'class':'md-textarea form-control', 'placeholder':'comment here...', 'rows':'4',}))# max max_length = required
