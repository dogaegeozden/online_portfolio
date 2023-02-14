# LIBRARIES
from django.db import models
from django.utils import timezone
# Importing the validators.
from django.core.validators import FileExtensionValidator
from custom_validators.validators import validate_file_size

# CLASSES
# Create your models here.

# A class to create meta description data model
class MetaDescription(models.Model):
    text = models.TextField(max_length=2000, null=False, blank=False, default="Click and see the certifications that I obtained from various platforms!", help_text="Meta description is a HTML element that describes the page's content. Creating a meta description element is beneficial for better SEO and that's why, you should use sentences which will catch the user's attention.")
    class Meta: # You are adding this to get rid of from the +s feature of django.https://docs.djangoproject.com/en/3.1/topics/db/models/ to see the feature search for "%(class" and you will see it's adding s.
        verbose_name_plural = "Meta Description"

# A class to create dynamic certification upload feature
class Certification(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False, default="Certification", help_text="Write the title of your certification.<br><strong>Hint: </strong>You can simply write the name of the certification.")# max max_length = required
    topic = models.CharField(max_length=300, null=False, blank=False, default="Topic", help_text="Write a topic which categorizes your application.<br><strong>Ex: </strong>Microsoft Office")# max max_length = required
    def upload_certification_image(self, field_attname):
        """A function which generates dynamic paths for certification images"""
        return f'certifications/{self.topic}/{self.image}'
    image = models.ImageField(null=False, blank=False, default="default.png", upload_to=upload_certification_image, help_text="<strong>Note: </strong><li>There is no specific required dimension.</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li><li>Make sure the file size is not over 30MB.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    alt = models.TextField(max_length=500, null=False, blank=False, default="Digital Marketer", verbose_name="ALT", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)
    class Meta: # You are adding this to get rid of from the +s feature of django.https://docs.djangoproject.com/en/3.1/topics/db/models/ to see the feature search for "%(class" and you will see it's adding s.
        verbose_name_plural = "Certifications"
    def __str__(self): # You are using this function to name data base objects so as long as there is this function the object that you created won't be named as Certifications object
        """String for representing the Model object."""
        return self.title

# A class to store certifications' page visits'
class CertificationPageVisit(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now) # To use django.utils.timezone utility properly you should have been set the TIME_ZONE in settings.py and set USE_TZ to True.
    class Meta:
        verbose_name_plural = 'Certification Page\'s Visit Information'
        ordering = ['-visit_time']

# A class to record certification clicks' in database in an organized format.
class CertificationClick(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    certification_choice = models.CharField(max_length=300, null=True, blank=True, verbose_name="Visitor's Certification Choice")
    click_time = models.DateTimeField(blank=True, null=True, verbose_name="Click Time", default=timezone.now)
    class Meta:
        verbose_name_plural = 'Certification Clicks'
        ordering = ['-click_time']
