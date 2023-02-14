# LIBRARIES
from django.db import models
from django.utils import timezone
# Importing the validators.
from django.core.validators import FileExtensionValidator
from custom_validators.validators import validate_file_size

# DATA CLASSES

# Creating a data class called MetaDescription to control how the objects will be created/stored in the database
class MetaDescription(models.Model):
    text = models.TextField(max_length=500, null=False, blank=False, default="Doga Ege Ozden's personal website and his online portfolio. This is the page where you can contact with him.")
    
    class Meta: # You are adding this to get rid of from the +s feature of django.https://docs.djangoproject.com/en/3.1/topics/db/models/ to see the feature search for "%(class" and you will see it's adding s.
        verbose_name_plural = "Meta Description"

# Creating a data class called ContactPic to control how the objects will be created/stored in the database
class ContactPPic(models.Model):
    image = models.ImageField(null=False, blank=False, default="default.png", upload_to="contact_page_pictures", help_text="<strong>Note: </strong><li>Required dimension ratio = 1.2 height/width</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li><li>Make sure the file size is not over 30MB.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    
    alt = models.TextField(max_length=500, null=False, blank=False, default="Django Web Developer", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).", verbose_name="ALT")
    
    class Meta: # You are adding this to get rid of from the +s feature of django.https://docs.djangoproject.com/en/3.1/topics/db/models/ to see the feature search for "%(class" and you will see it's adding s.
        verbose_name_plural = "Contact Page Picture"

# Creating a data class called Message to control how the objects will be created/stored in the database
class Message(models.Model):
    first_name = models.CharField(max_length=250, verbose_name="First Name")# max max_length = required
    
    last_name = models.CharField(max_length=250, default='N/A', verbose_name="Last Name")# max max_length = required
    
    email = models.EmailField(max_length=350, verbose_name="E-mail")
    
    phone_number = models.CharField(max_length=100, default='N/A', verbose_name="Phone Number")
    
    message = models.TextField(max_length=7500, verbose_name="Message")
    
    message_sending_time = models.DateTimeField(blank=True, null=True, verbose_name="Submit Time", default=timezone.now) # To use django.utils.timezone utility properly you should have been set the TIME_ZONE in settings.py and set USE_TZ to True.
    
    ip_address = models.GenericIPAddressField(null=True, blank=True, default='N/A',)
    
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)

# Creating a data class called ContactPageVisit to control how the objects will be created/stored in the database
class ContactPageVisit(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now) # To use django.utils.timezone utility properly you should have been set the TIME_ZONE in settings.py and set USE_TZ to True.
    
    class Meta:
        verbose_name_plural = 'Contact Pages\' Visit Information'
        ordering = ['-visit_time']
