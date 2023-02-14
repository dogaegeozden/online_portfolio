# LIBRARIES
from django.contrib import admin
# MODELS
from .models import MetaDescription, ProfilePic, Bio, ToolOrLanguage, ToolsOrLanguagesMainVisual, Activity, SocialMediaLinks, MainPageVisit, SocialMediaButtonClick, ActivityImageClick, ProfilePictureClick, ToolsAndLanguagesImageClick

# Registering the MetaDescription data model to the admin panel.
@admin.register(MetaDescription)
class MetaDescriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',) # You should put "," after first item or else python won't recognize it as tuple.
        }),
    )

# Registering the ProfilePic data model to the admin panel.
@admin.register(ProfilePic)
class ProfilePic(admin.ModelAdmin):
    fieldsets = (
        ('Profile Picture', {
            'fields': ('image',)
        }),
        ('SEO (Search Engine Optimization) | Alt (Alternative Text): To make pictures accessable with texts', {
            'fields': ('alt',)
        }),
    )

# Registering the Bio data model to the admin panel.
@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    fieldsets = (
        ('BIO (Biography)', {
            'fields': ('text',)
        }),
    )

# Registering the ToolsOrLanguagesMainVisual data model to the admin panel.
@admin.register(ToolsOrLanguagesMainVisual)
class ToolsAndLanguagesAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Tools And Languages Section\'s Main Visual', {
            'fields': ('title', 'image', 'alt',)
        }),
    )

# Registering the ToolOrLanguage data model to the admin panel.
@admin.register(ToolOrLanguage)
class ToolOrLanguageAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Tool or Language', {
            'fields': ('title', 'icon_url', 'alt',)
        }),
    )

# Registering the Activity data model to the admin panel.
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Activity Information & Content', {
            'fields': ('title', 'description', 'image')
        }),
        ('SEO (Search Engine Optimization) | Alt (Alternative Text): To make pictures accessable with texts', {
            'fields': ('alt',)
        }),
    )

# Registering the SocialMediaLinks data model to the admin panel.
@admin.register(SocialMediaLinks)
class SocialMediaLinksAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Social Media Links', {
            'fields': ('linkedin', 'instagram', 'facebook', 'github', 'googleplay', 'email', 'slideshare')
        }),
    )

# Registering the MainPageVisit data model to the admin panel.
@admin.register(MainPageVisit)
class MainPageVisitAdmin(admin.ModelAdmin):
    readonly_fields = ('ip_address', 'visit_time', 'user_agent',)
    fieldsets = (
        ('Main Page Visitor\'s Information', {
            'fields': ('ip_address', 'visit_time', 'user_agent',)
        }),
    )

# Registering the SocialMediaButtonClick data model to the admin panel.
@admin.register(SocialMediaButtonClick)
class SocialMediaButtonClickAdmin(admin.ModelAdmin):
    readonly_fields = ('ip_address', 'click_time', 'user_agent', 'platform_choice',)
    fieldsets = (
        ('Social Media Button Click', {
            'fields': ('ip_address', 'click_time', 'user_agent', 'platform_choice',)
        }),
    )

# Registering the ActivityImageClick data model to the admin panel.
@admin.register(ActivityImageClick)
class ActivityImageClickAdmin(admin.ModelAdmin):
    readonly_fields = ('ip_address', 'click_time', 'user_agent', 'activity_image_choice',)
    fieldsets = (
        ('Activity Image Click', {
            'fields': ('ip_address', 'click_time', 'user_agent', 'activity_image_choice',)
        }),
    )

# Registering the ProfilePictureClick data model to the admin panel.
@admin.register(ProfilePictureClick)
class ProfilePictureClickAdmin(admin.ModelAdmin):
    readonly_fields = ('ip_address', 'click_time', 'user_agent', 'profile_picture_choice',)
    fieldsets = (
        ('Profile Picture Click', {
            'fields': ('ip_address', 'click_time', 'user_agent', 'profile_picture_choice',)
        }),
    )

# Registering the ToolsAndLanguagesImageClick data model to the admin panel.
@admin.register(ToolsAndLanguagesImageClick)
class ToolsAndLanguagesImageClickAdmin(admin.ModelAdmin):
    readonly_fields = ('ip_address', 'click_time', 'user_agent', 'tools_and_languages_image_choice',)
    fieldsets = (
        ('Tools And Languages Image Click', {
            'fields': ('ip_address', 'click_time', 'user_agent', 'tools_and_languages_image_choice',)
        }),
    )
