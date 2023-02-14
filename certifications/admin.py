# LIBRARIES
from django.contrib import admin
# MODELS
from .models import MetaDescription, Certification, CertificationPageVisit, CertificationClick

# DATA CLASSES

# Registering the MetaDescription data model to the admin panel
@admin.register(MetaDescription)
class MetaDescriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',) # You should put "," after first item or else python won't recognize it as tuple.
        }),
    )

# Registering the Certification data model to the admin panel
@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic')
    list_filter = ('title', 'topic')
    fieldsets = (
        ('Certificate Information & Content', {
            'fields': ('title', 'topic', 'image',)
        }),
        ('SEO (Search Engine Optimization) | Alt (Alternative Text): To make pictures accessable with texts', {
            'fields': ('alt',) # You should put "," after first item or else python won't recognize it as tuple.
        }),
    )

# Registering the CertificationPageVisit data model to the admin panel
@admin.register(CertificationPageVisit)
class CertificationPageVisitAdmin(admin.ModelAdmin):
    readonly_fields = ('ip_address', 'visit_time', 'user_agent',)
    fieldsets = (
        ('Main Page Visitor\'s Information', {
            'fields': ('ip_address', 'visit_time', 'user_agent',)
        }),
    )

# Registering the CertificationClick data model to the admin panel
@admin.register(CertificationClick)
class CertificationClickAdmin(admin.ModelAdmin):
    readonly_fields = ('ip_address', 'click_time', 'user_agent', 'certification_choice',)
    fieldsets = (
        ('Social Media Button Click', {
            'fields': ('ip_address', 'click_time', 'user_agent', 'certification_choice',)
        }),
    )
