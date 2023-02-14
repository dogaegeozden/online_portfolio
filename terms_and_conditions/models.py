# LIBRARIES
from django.db import models
from django.utils import timezone

# DATA CLASSES

# Creating a data modeal called MetaDescription to control how the objects will be created/stored in the database.
class MetaDescription(models.Model):
    text = models.TextField(max_length=500, null=False, blank=False, default="Your privayc is important to me.",)
    class Meta:
        verbose_name_plural = "Meta Description"

# Creating a data modeal called TermsAndConditionsPageVisit to control how the objects will be created/stored in the database.
class TermsAndConditionsPageVisit(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now) # To use django.utils.timezone utility properly you should have been set the TIME_ZONE in settings.py and set USE_TZ to True.

    class Meta:
        verbose_name_plural = 'Terms And Conditions Page\'s Visit Information'
        ordering = ['-visit_time']
