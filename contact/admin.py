# LIBRARIES
from django.contrib import admin
# MODELS
from contact.models import MetaDescription, ContactPPic, Message, ContactPageVisit

# Registering the MetaDescription data model to the admin panel.
@admin.register(MetaDescription)
class MetaDescriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',) # You should put "," after first item or else python won't recognize it as tuple.
        }),
    )

# Registering the ContactPPic data model to the admin panel.
@admin.register(ContactPPic)
class ContactPPicAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Contact Page Picture', {
            'fields': ('image',)
        }),
        ('SEO (Search Engine Optimization) | Alt (Alternative Text): To make pictures accessable with texts', {
            'fields': ('alt',) # You should put "," after first item or else python won't recognize it as tuple.
        }),
    )

# Registering the Message data model to the admin panel.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    readonly_fields=('first_name', 'last_name', 'email', 'phone_number', 'message', 'message_sending_time', 'ip_address', 'user_agent',) # These fields cannot be edited from admin page.
    fieldsets = (
        ('Message', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number', 'message', 'message_sending_time', 'ip_address', 'user_agent',)
        }),
    )

# Registering the ContactPageVisit data model to the admin panel.
@admin.register(ContactPageVisit)
class ContactPageVisitAdmin(admin.ModelAdmin):
    readonly_fields = ('ip_address', 'visit_time', 'user_agent',)
    fieldsets = (
        ('Post Detail Page Visitor\'s Information', {
            'fields': ('ip_address', 'visit_time', 'user_agent',)
        }),
    )
