# LIBRARIES
from django.contrib import admin
# MODELS
from .models import MetaDescription, AboutCurrentPosition, Experience, Education, Resume, ResumePageVisit, ResumeFileClicks

# Registering the Resume data class to the admin panel.
@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Resume Information & Content', {
            'fields': ('field_name', 'resume_name', 'file',)
        }),
    )

# Registering the MetaDescription data class to the admin panel.
@admin.register(MetaDescription)
class MetaDescriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',) # You should put "," after first item or else python won't recognize it as tuple.
        }),
    )

# Registering the AboutCurrentPosition data class to the admin panel.
@admin.register(AboutCurrentPosition)
class AboutCurrentPositionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Text About Your Current Position in Your Career', {
            'fields': ('text',) # You should put "," after first item or else python won't recognize it as tuple.
        }),
    )

# Registering the Experience data class to the admin panel.
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company_name', 'start_date', 'end_date', 'working_status')
    list_filter = ('job_title', 'company_name', 'start_date', 'end_date', 'working_status')
    fieldsets = (
        ('Job Information', {
            'fields': ('job_title', 'company_name', 'text', 'header', 'list_item_1', 'list_item_2', 'list_item_3', 'list_item_4', 'list_item_5','img_1', 'img_2', 'img_3', 'img_4', 'img_5', 'img_6', 'img_7', 'img_8', 'img_9', 'img_10',)
        }),
        ('Working Status', {
            'fields': ('start_date', 'end_date', 'working_status')
        }),
    )

# Registering the Education data class to the admin panel.
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Education Information', {
            'fields': ('name', 'city', 'province', 'start_date', 'end_date', 'major', 'diploma', 'para',)
        }),
        ('SEO (Search Engine Optimization) | Alt (Alternative Text): To make pictures accessable with texts', {
            'fields': ('alt',) # You should put "," after first item or else python won't recognize it as tuple.
        }),
    )

# Registering the ResumePageVisit data class to the admin panel.
@admin.register(ResumePageVisit)
class ResumePageVisitAdmin(admin.ModelAdmin):
    readonly_fields = ('ip_address', 'visit_time', 'user_agent',)
    fieldsets = (
        ('Resume Page\'s Visitor\'s Information', {
            'fields': ('ip_address', 'visit_time', 'user_agent',)
        }),
    )

# Registering the ResumeFileClicks data class to the admin panel.
@admin.register(ResumeFileClicks)
class ResumeFileClicksAdmin(admin.ModelAdmin):
    readonly_fields = ('resume_choice', 'ip_address', 'click_time', 'user_agent',)
    fieldsets = (
        ('Resume File Click Information', {
            'fields': ('resume_choice', 'ip_address', 'click_time', 'user_agent',)
        }),
    )
