# LIBRARIES
from django.db import models
from django.utils import timezone
import uuid
from django.urls import reverse
from embed_video.fields import EmbedVideoField
# Importing the validators.
from django.core.validators import FileExtensionValidator
from custom_validators.validators import validate_file_size

# Creating a class called MetaDescription to control how the objects will be created/stored in the database.
class MetaDescription(models.Model):
    text = models.TextField(max_length=2000, null=False, blank=False, default="Doga Ege Ozden's blog where he shares his posts. Where you can learn what he is currently doing.", help_text="Meta description is a HTML element that describes the page's content. Creating a meta description element is beneficial for better SEO and that's why, you should use sentences which will catch the user's attention.",)
    
    class Meta: # You are adding this to get rid of from the +s feature of django.https://docs.djangoproject.com/en/3.1/topics/db/models/ to see the feature search for "%(class" and you will see it's adding s.
        verbose_name_plural = "Meta Description"

# Creating a class called BlogPost to control how the objects will be created/stored in the database.
class BlogPost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name="ID", help_text="Universal Unique Identifier")
    
    title = models.CharField(max_length=300, null=False, blank=False, default="Title", help_text="Write a title for your post.<br><strong>Note: </strong><li>Keep it concise and informative</li><li>Write for your audience</li><li>Entice the reader</li><li>Incorporate important keywords</li><li>Write in sentence case</li>")# max max_length = required

    def upload_post_image(self, field_attname):
        """A function which generates dynamic paths for post images."""
        return f'blog/{self.title}/{self.image}'
    
    image = models.ImageField(null=True, blank=True, upload_to=upload_post_image, help_text="<strong>Note: </strong><li>There is no specific required dimension.</li><li>Accepted file types are png, jpg and, jpeg.</li><li>You can use GIMP to change file type/extension.</li><li>Make sure the file size is not over 30MB.</li>", validators=[FileExtensionValidator(['png', 'jpg', 'jpeg']), validate_file_size],)
    
    def upload_post_video(self, field_attname):
        """A function which generates dynamic paths for post videos."""
        return f'blog/{self.title}/{self.image}'

    video = models.FileField(null=True, blank=True, upload_to=upload_post_video, help_text="Upload image or video. This application can't display both. (Prefferred image)")

    youtube_url = EmbedVideoField(max_length=1000, null=True, blank=True, help_text="<strong>Note: </strong><li>Open the video from YouTube. Press to the share > embed. Only copy paste the url that's 'src' attributes value.</li><li><strong>Ex: </strong>'https://www.youtube.com/embed/el1t1FoWdZI'</li><li><strong>Hint: Without quotes.</li>")
    
    date = models.DateField(auto_now_add=False, null=True, blank=True, help_text="Please use the fallowing format: YYYY-MM-DD")
    
    text = models.TextField(max_length=10000, null=False, blank=False, help_text="<strong>Note: </strong><li>Make sure to avoid repetition</li><li>Make sure your post has introduction, body and conclusion</li><li>Use short paragraps</li><li>Write an empathic introduction</li><li>Read your post aloud to check its flow</li><li>Have some sort of call to action in the end.</li>")
    
    alt = models.TextField(max_length=500, null=False, blank=False, default="Blog Post", verbose_name="ALT", help_text="The alt attribute provides alternative information for an image if a user for some reason cannot view it (because of slow connection, an error in the src attribute, or if the user uses a screen reader).",)
    
    class Meta: # You are adding this to get rid of from the +s feature of django.https://docs.djangoproject.com/en/3.1/topics/db/models/ to see the feature search for "%(class" and you will see it's adding s.
        verbose_name_plural = "Posts"
        ordering = ['-date']
    
    def __str__(self):
        """A function which returns a string which will represent the object. Hint: Now, when you crated an object these object will be named with the object's title instead of Object (1) or (2)"""
        return self.title
    
    def get_absolute_url(self):
        """A function which returns the url to access a particular book instance."""
        return reverse('post-detail', args=[str(self.id)])

# Creating a class called Subscription to control how the objects will be created/stored in the database.
class Subscription(models.Model):
    email = models.EmailField(max_length=350, verbose_name="E-Mail",)

    ip_address = models.GenericIPAddressField(null=True, blank=True, default='N/A', verbose_name="Ip Address")
    
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    
    subscription_time = models.DateTimeField(blank=True, null=True, verbose_name="Subscribe Time", default=timezone.now) # To use django.utils.timezone utility properly you should have been set the TIME_ZONE in settings.py and set USE_TZ to True.
    
    class Meta: # You are adding this to get rid of from the +s feature of django.https://docs.djangoproject.com/en/3.1/topics/db/models/ to see the feature search for "%(class" and you will see it's adding s.
        verbose_name_plural = "Subscriptions"
    
    def __str__(self):
        """A function which returns a string which will represent the object. Hint: Now, when you crated an object these object will be named with the object's title instead of Object (1) or (2)"""
        return self.email

# Creating a class called Comment to control how the objects will be created/stored in the database.
class Comment(models.Model):
    post = models.ForeignKey('BlogPost', null=True, blank=True, related_name="comments", on_delete=models.CASCADE)
    
    name = models.CharField(max_length=150, null=False, blank=False,)
    
    text = models.TextField(max_length=1500, null=True, blank=True,)
    
    comment_time = models.DateTimeField(blank=True, null=True, verbose_name="Comment Time", default=timezone.now)
    
    ip_address = models.GenericIPAddressField(null=True, blank=True, default='N/A', verbose_name="Ip Address")
    
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    
    def __str__(self):
        """A function which returns a string which will represent the object. Hint: Now, when you crated an object these object will be named with the object's title instead of Object (1) or (2)"""
        return '%s - %s' % (self.post.title, self.name)

# Creating a class called BlogPageVisit to control how the objects will be created/stored in the database.
class BlogPageVisit(models.Model):
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now) # To use django.utils.timezone utility properly you should have been set the TIME_ZONE in settings.py and set USE_TZ to True.
    
    class Meta:
        verbose_name_plural = 'Blog Page\'s Visit Information'
        ordering = ['-visit_time']

# Creating a class called PostDetailPageVisit to control how the objects will be created/stored in the database.
class PostDetailPageVisit(models.Model):
    uuid = models.CharField(max_length=500, null=False, blank=False, verbose_name="Universal Unique Identifier",)
    
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    
    visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Visit Time", default=timezone.now) # To use django.utils.timezone utility properly you should have been set the TIME_ZONE in settings.py and set USE_TZ to True.
    
    class Meta:
        verbose_name_plural = 'Post Detail Pages\' Visit Information'
        ordering = ['-visit_time']

# Creating a class called PostLike to control how the objects will be created/stored in the database.
class PostLike(models.Model):
    post = models.ForeignKey('BlogPost', null=True, blank=True, related_name="likes", on_delete=models.CASCADE)
    
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    
    like_time = models.DateTimeField(blank=True, null=True, verbose_name="Like Time", default=timezone.now) # To use django.utils.timezone utility properly you should have been set the TIME_ZONE in settings.py and set USE_TZ to True.
    
    like_status_options = (
        ('l', 'Liked'),
        ('n', 'Not Liked'),
    )
    
    like_status = models.CharField(max_length=1, choices=like_status_options, blank=False, default='n', verbose_name="Like Status")
    
    class Meta:
        verbose_name_plural = 'Posts\' Like Information'
        ordering = ['-like_time']

# Creating a class called ShareClick to control how the objects will be created/stored in the database.
class ShareClick(models.Model):
    uuid = models.CharField(max_length=500, null=False, blank=False, verbose_name="Universal Unique Identifier",)
    
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Ip Address", default='N/A',)
    
    user_agent = models.CharField(max_length=5000, null=True, blank=True, verbose_name="User Agent", default="N/A",)
    
    click_time = models.DateTimeField(blank=True, null=True, verbose_name="Click Time", default=timezone.now) # To use django.utils.timezone utility properly you should have been set the TIME_ZONE in settings.py and set USE_TZ to True.
    
    platform_choice = models.CharField(max_length=200, null=True, blank=True, verbose_name="Visitor's Platform Choice To Share The Post")
    
    class Meta:
        verbose_name_plural = 'Share Buttons\' Click Data'
        ordering = ['-click_time']
