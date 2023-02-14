# LIBRARIES
from django.contrib import admin
# MODELS
from .models import MetaDescription, GraphicDesign, WebDevelopment, WorksPageVisit, GraphicDesignProjClickData, WebDevProjClickData

# Registering the MetaDescription data class to the admin panel
@admin.register(MetaDescription)
class MetaDescriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',)
        }),
    )

# Registering the GraphicDesign data class to the admin panel
@admin.register(GraphicDesign)
class GraphicDesignAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Visuals', {
            'fields': ('name', 'image', 'video', 'youtube_url',)
        }),
        ('SEO (Search Engine Optimization) | Alt (Alternative Text): To make pictures accessable with texts', {
            'fields': ('alt',)
        }),
    )

# Registering the WebDevelopment data class to the admin panel
@admin.register(WebDevelopment)
class WebDevelopmentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Web Development', {
            'fields': ('title', 'web_page_link',)
        }),
    )

# Registering the WorksPageVisit data class to the admin panel
@admin.register(WorksPageVisit)
class WorksPageVisitAdmin(admin.ModelAdmin):
    readonly_fields = ('ip_address', 'visit_time', 'user_agent',)
    fieldsets = (
        ('Works Page\'s Visitor\'s Information', {
            'fields': ('ip_address', 'visit_time', 'user_agent',)
        }),
    )

# Registering the GraphicDesignProjClickData data class to the admin panel
@admin.register(GraphicDesignProjClickData)
class GraphicDesignProjClickDataAdmin(admin.ModelAdmin):
    readonly_fields = ('project_choice', 'ip_address', 'click_time', 'user_agent',)
    fieldsets = (
        ('Works Page\'s Visitor\'s Information', {
            'fields': ('project_choice', 'ip_address', 'click_time', 'user_agent',)
        }),
    )

# Registering the WebDevProjClickData data class to the admin panel
@admin.register(WebDevProjClickData)
class WebDevProjClickDataAdmin(admin.ModelAdmin):
    readonly_fields = ('project_choice', 'ip_address', 'click_time', 'user_agent',)
    fieldsets = (
        ('Works Page\'s Visitor\'s Information', {
            'fields': ('project_choice', 'ip_address', 'click_time', 'user_agent',)
        }),
    )
