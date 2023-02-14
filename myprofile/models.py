# LIBRARIES
from django.db import models
from django.utils import timezone
# Importing the validators.
from django.core.validators import FileExtensionValidator
from custom_validators.validators import validate_file_size

# DATA CLASSES
# Creating a data class called MetaDescription to control how objects will be created/stored in the database.
class MetaDescription(models.Model):
    text = models.TextField(max_length=2000, null=False, blank=False, default="Doga Ege Ozden's online portfolio. Click and check out the activities that he is interested, his bio and etc.", help_text="Meta description is a HTML element that describes the page's content. Creating a meta description element is beneficial for better SEO and that's why, you should use sentences which will catch the user's attention.",)
    class Meta: # You are adding this to get rid of from the +s feature of django.https://docs.djangoproject.com/en/3.1/topics/db/models/ to see the feature search for "%(class" and you will see it's adding s.
        verbose_name_plural = "Meta Description"

# Creating a data class called ProfilePic to control how objects will be created/stored in the database.
class ProfilePic(models.Model):
    image = models.ImageField(null=False, blank=False, default="default.png", upload_to='profile_pictures', help_text="<strong>Note: </strong><li>Dimension requirement is 1.3 height/width</li><li>Accepted file types are png, jpg and, jpeg</li><li>You can use GIMP to change the file type/extension</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size])
    alt = models.TextField(max_length=500, null=False, blank=False, default="Marketing Manager", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).", verbose_name="ALT")
    class Meta: # You are adding this to get rid of from the +s feature of django.https://docs.djangoproject.com/en/3.1/topics/db/models/ to see the feature search for "%(class" and you will see it's adding s.
        verbose_name_plural = "Profile Picture"

# Creating a data class called Bio to control how objects will be created/stored in the database.
class Bio(models.Model):
    text = models.TextField(max_length=10000, blank=False, null=False, default="My name is Doga. I'm a full-stack web developer from Turkey. I'm highly motivated, disciplined and enthusiastic. I enjoy reading self development, science fiction and fantasy books, programming and, calisthenics.", help_text="<strong>Notes: </strong><li>Introduce your self.</li><li>Include the most relevant professional experience.</li><li>Mention significant personal achievements or awards.</li><li>Introduce personal details.</li><li>Use a casual and friendly tone.</li>")
    class Meta: # You are adding this to get rid of from the +s feature of django.https://docs.djangoproject.com/en/3.1/topics/db/models/ to see the feature search for "%(class" and you will see it's adding s.
        verbose_name_plural = "Bio"

# Creating a data class called ToolsOrLanguagesMainVisual to control how objects will be created/stored in the database.
class ToolsOrLanguagesMainVisual(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False, default="TOOLS AND LANGUAGES", help_text="Create a title for the tools and languages section.")
    image = models.ImageField(null=False, blank=False, default="default.png", upload_to='tools_and_languages_main_visuals', help_text="<strong>Note: </strong><li>Required dimension ratio = 1.2 height/width</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change the file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    alt = models.TextField(max_length=500, null=False, blank=False, default="digital nomad", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).", verbose_name="ALT")
    class Meta:
        verbose_name_plural = "Tools And Languages' Section's Main Visual"
    def __str__(self):
        """A function that names the object with it's title"""
        return self.title

# Creating a data class called ToolOrLanguage to control how objects will be created/stored in the database.
class ToolOrLanguage(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False, default="Programming Language", help_text="Create a title for the tool or language object.")
    icon_url = models.URLField(max_length=1000, null=True, blank=True, verbose_name="URL", help_text="Copy paste the url which leads to the tool's or language's icon.")
    alt = models.TextField(max_length=500, null=False, blank=False, default="self taught programmer", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).", verbose_name="ALT")
    class Meta:
        verbose_name_plural = "Tools And Languages"
    def __str__(self):
        """A function that names the object with it's title"""
        return self.title

# Creating a data class called Activity to control how objects will be created/stored in the database.
class Activity(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False, default="Activity Title", help_text="Give a title to the activiy.<br>Note: You can use the activity's name.<br>Ex: Calisthenics")
    description = models.TextField(max_length=2000, null=True, blank=True, default="None",)
    def upload_activity_img(self, field_attname):
        """A function which creates a path to upload images."""
        return f'myprofile/activities/{self.title}/{self.image}'
    image = models.ImageField(null=False, blank=False, default="default.png", upload_to=upload_activity_img, help_text="<strong>Note: </strong><li>Required Dimension Ratio = 1.2 height/width</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    alt = models.TextField(max_length=500, null=False, blank=False, default="Brand Manager", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).", verbose_name="ALT")
    class Meta: # You are adding this to get rid of from the +s feature of django.https://docs.djangoproject.com/en/3.1/topics/db/models/ to see the feature search for "%(class" and you will see it's adding s.
        verbose_name_plural = "Activity"
    def __str__(self):
        """A function that names the object with it's title."""
        return self.title

# Creating a data class called SocialMediaLinks to control how objects will be created/stored in the database.
class SocialMediaLinks(models.Model):
    linkedin = models.URLField(max_length=1000, null=True, blank=True, verbose_name="LinkedIn")
    instagram = models.URLField(max_length=1000, null=True, blank=True,)
    facebook = models.URLField(max_length=1000, null=True, blank=True,)
    github = models.URLField(max_length=1000, null=True, blank=True, verbose_name="GitHub")
    googleplay = models.URLField(max_length=1000, null=True, blank=True, verbose_name="Google Play")
    email = models.URLField(max_length=1000, null=True, blank=True, verbose_name="E-Mail")
    slideshare = models.URLField(max_length=1000, null=True, blank=True, verbose_name="Slide Share")
    class Meta: # You are adding this to get rid of from the +s feature of django.https://docs.djangoproject.com/en/3.1/topics/db/models/ to see the feature search for "%(class" and you will see it's adding s.
        verbose_name_plural = "Social Media Links"

# Creating a data class called MainPageVisit to control how objects will be created/stored in the database.
class MainPageVisit(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now) # To use django.utils.timezone utility properly you should have been set the TIME_ZONE in settings.py and set USE_TZ to True.
    class Meta:
        verbose_name_plural = 'Main Page\'s Visit Information'
        ordering = ['-visit_time']

# Creating a data class called SocialMediaButtonClick to control how objects will be created/stored in the database.
class SocialMediaButtonClick(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    platform_choice = models.CharField(max_length=300, null=True, blank=True, verbose_name="Visitor's Platform Choice")
    click_time = models.DateTimeField(blank=True, null=True, verbose_name="Click Time", default=timezone.now)
    class Meta:
        verbose_name_plural = 'Social Media Button Clicks'
        ordering = ['-click_time']

# Creating a data class called ProfilePictureClick to control how objects will be created/stored in the database.
class ProfilePictureClick(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    profile_picture_choice = models.CharField(max_length=300, null=True, blank=True, verbose_name="Profile Picture Choice")
    click_time = models.DateTimeField(blank=True, null=True, verbose_name="Click Time", default=timezone.now)
    class Meta:
        verbose_name_plural = 'Profile Picture Clicks'
        ordering = ['-click_time']

# Creating a data class called ToolsAndLanguagesImageClick to control how objects will be created/stored in the database.
class ToolsAndLanguagesImageClick(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    tools_and_languages_image_choice = models.CharField(max_length=300, null=True, blank=True, verbose_name="Visitor's Tools And Languages Image Choice")
    click_time = models.DateTimeField(blank=True, null=True, verbose_name="Click Time", default=timezone.now)
    class Meta:
        verbose_name_plural = 'Tools And Languages Image Clicks'
        ordering = ['-click_time']

# Creating a data class called ActivityImageClick to control how objects will be created/stored in the database.
class ActivityImageClick(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    activity_image_choice = models.CharField(max_length=300, null=True, blank=True, verbose_name="Visitor's Activity Image Choice")
    click_time = models.DateTimeField(blank=True, null=True, verbose_name="Click Time", default=timezone.now)
    class Meta:
        verbose_name_plural = 'Activity Image Clicks'
        ordering = ['-click_time']

