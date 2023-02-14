# LIBRARIES
from django.db import models
from django.utils import timezone
# Importing the validators.
from django.core.validators import FileExtensionValidator
from custom_validators.validators import validate_file_size

# DATA CLASSES

# Creating a class called MetaDescription to control how the objects will be created/stored in the database.
class MetaDescription(models.Model):
    text = models.TextField(max_length=1000, null=False, blank=False, default="Highlighted photo edits, edited videos, web development projects and works of Doga Ege Ozden.", help_text="Meta description is a HTML element that describes the page's content. Creating a meta description element is beneficial for better SEO and that's why, you should use sentences which will catch the user's attention.",)
    
    class Meta: # You are adding this to get rid of from the +s feature of django.https://docs.djangoproject.com/en/3.1/topics/db/models/ to see the feature search for "%(class" and you will see it's adding s.
        verbose_name_plural = "Meta Description"

# Creating a class called GraphicDesign to control how the objects will be created/stored in the database.
class GraphicDesign(models.Model):
    name = models.CharField(max_length=300, unique=True, null=False, blank=False, default="Web Application", help_text="Name the visual.<br><strong>Note:</strong>Make sure each visual has a unique name.")
    
    def upload_graphic_design_image(self, field_attname):
        """A function which generates dynamic paths for graphic design images."""
        return f'works/{self.name}/{self.image}'

    image = models.ImageField(null=True, blank=True, upload_to=upload_graphic_design_image, help_text="<strong>Notes: </strong><li>There is no specific dimension requirement.</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)

    def upload_graphic_design_video(self, field_attname):
        """A function which generates dynamic paths for graphic design video files."""
        return f'works/{self.name}/{self.video}'

    video = models.FileField(null=True, blank=True, upload_to=upload_graphic_design_video, help_text="<strong>Notes: </strong><li>All videos has to be in mp4 format</li><li>You can convert videos to mp4 format using Blender.</li><li>File size should not exceed 30MB.</li>",  validators=[FileExtensionValidator(['mp4']), validate_file_size])
    
    youtube_url = models.URLField(max_length=500, null=True, blank=True, help_text="<strong>Note:</strong><li>Only copy paste the url which is the 'src' attribute's value from the iframe which will be embedded.<br>Ex-url: 'https://www.youtube.com/embed/rSyNTBy2MQY'<br>Hint: Without quotes.</li>", verbose_name="YouTube URL")
    
    alt = models.TextField(max_length=500, null=False, blank=False, default="Graphic designer", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).", verbose_name="ALT")
    
    class Meta:
        verbose_name_plural = "Graphic Design"

# Creating a class called WebDevelopment to control how the objects will be created/stored in the database.
class WebDevelopment(models.Model):
    title = models.CharField(max_length=300, unique=True, null=False, blank=False, default="Web Application", help_text="Write the name of the project.")
    
    web_page_link = models.URLField(max_length=750, null=False, blank=False, default="https://tamrinotte.pythonanywhere.com/", help_text="<li>Copy paste the project page's link</li>", verbose_name="Web Page Link")
    
    class Meta:
        verbose_name_plural = "Web Development"

    def __str__(self):
        return self.title

# Creating a class called WorksPageVisit to control how the objects will be created/stored in the database.
class WorksPageVisit(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now)
    
    class Meta:
        verbose_name_plural = 'Works Page\'s Visit Information'
        ordering = ['-visit_time']

# Creating a class called GraphicDesignProjClickData to control how the objects will be created/stored in the database.
class GraphicDesignProjClickData(models.Model):
    project_choice = models.CharField(max_length=300, null=True, blank=True, verbose_name="Visitor's Project Choice")
    
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    
    click_time = models.DateTimeField(blank=True, null=True, verbose_name="Click Time", default=timezone.now)
    
    class Meta:
        verbose_name_plural = "Graphic Design Project Click Data"
        ordering = ["-click_time"]

# Creating a class called WebDevProjClickData to control how the objects will be created/stored in the database.
class WebDevProjClickData(models.Model):
    project_choice = models.CharField(max_length=300, null=True, blank=True, verbose_name="Visitor's Project Choice")
    
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    
    click_time = models.DateTimeField(blank=True, null=True, verbose_name="Click Time", default=timezone.now)
    
    class Meta:
        verbose_name_plural = "Web Development Project Link Click Data"
        ordering = ["-click_time"]
