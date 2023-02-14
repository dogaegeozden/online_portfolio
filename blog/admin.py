# LIBRARIES
from django.contrib import admin
# MODELS
from .models import MetaDescription, BlogPost, Subscription, Comment, BlogPageVisit, PostDetailPageVisit, PostLike, ShareClick

# Registering the MetaDescription model to the admin panel
@admin.register(MetaDescription)
class MetaDescriptionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('SEO (Search Engine Optimization) | Meta Description : Description of the page', {
            'fields': ('text',) # You should put "," after first item or else python won't recognize it as tuple.
        }),
    )

# Registering the BlogPost model to the admin panel
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ('title', 'date')
    readonly_fields=('id',)
    fieldsets = (
        ('Post Information & Content', {
            'fields': ('title', 'image', 'youtube_url', 'video', 'date', 'text','id',)
        }),
        ('SEO (Search Engine Optimization) | Alt (Alternative Text): To make pictures accessable with texts', {
            'fields': ('alt',) # You should put "," after first item or else python won't recognize it as tuple.
        }),
    )

# Registering the Comment model to the admin panel
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    readonly_fields=('ip_address', 'comment_time', 'user_agent',)
    fieldsets = (
        ('Comments', {
            'fields': ('name', 'text', 'comment_time', 'post', 'ip_address', 'user_agent',)
        }),
    )

# Registering the Subscription model to the admin panel
@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    readonly_fields=('email', 'subscription_time', 'ip_address',) # These fields cannot be edited from admin page.
    fieldsets = (
        ('Message', {
            'fields': ('email', 'subscription_time', 'ip_address',)
        }),
    )

# Registering the BlogPageVisit model to the admin panel
@admin.register(BlogPageVisit)
class BlogPageVisitAdmin(admin.ModelAdmin):
    readonly_fields = ('ip_address', 'visit_time', 'user_agent',)
    fieldsets = (
        ('Blog Page\'s Visitors\' Information', {
            'fields': ('ip_address', 'visit_time', 'user_agent',)
        }),
    )

# Registering the PostDetailPageVisit model to the admin panel
@admin.register(PostDetailPageVisit)
class PostDetailPageVisitAdmin(admin.ModelAdmin):
    readonly_fields = ('ip_address', 'visit_time', 'user_agent',)
    fieldsets = (
        ('Post Detail Page\'s Visitors\' Information', {
            'fields': ('ip_address', 'visit_time', 'user_agent',)
        }),
    )

# Registering the PostLike data model to the admin panel
@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    readonly_fields = ('post', 'ip_address', 'user_agent', 'like_time', 'like_status',)
    fieldsets = (
        ('Post Detail Page\'s Visitors\' Information', {
            'fields': ('post', 'ip_address', 'like_time', 'user_agent', 'like_status',)
        }),
    )

# Registering the ShareClick model to the admin panel
@admin.register(ShareClick)
class ShareClickAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid', 'ip_address', 'user_agent', 'click_time', 'platform_choice',)
    fieldsets = (
        ('Post Share Buttons\' Click Information', {
            'fields': ('uuid', 'ip_address', 'user_agent', 'click_time', 'platform_choice',)
        }),
    )
