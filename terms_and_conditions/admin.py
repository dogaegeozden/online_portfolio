# LIBRARIES
from django.contrib import admin
# MODELS
from .models import MetaDescription, TermsAndConditionsPageVisit

# Registering the MetaDescription model to the admin panel.
@admin.register(MetaDescription)
class MetaDescriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',) # You should put "," after first item or else python won't recognize it as tuple.
        }),
    )

# Registering the TermsAndConditionsPageVisit model to the admin panel.
@admin.register(TermsAndConditionsPageVisit)
class TermsAndConditionsPageVisitAdmin(admin.ModelAdmin):
    readonly_fields = ('ip_address', 'visit_time', 'user_agent',)
    fieldsets = (
        ('Terms And Conditions Page\'s Visitor\'s Information', {
            'fields': ('ip_address', 'visit_time', 'user_agent',)
        }),
    )
