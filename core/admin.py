from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    actions = ['confirm_posts', 'publish_posts']

    def confirm_posts(self, request, queryset):
        queryset.update(status='confirmed')
    confirm_posts.short_description = 'Confirm selected posts'

    def publish_posts(self, request, queryset):
        queryset.filter(status='confirmed').update(status='published')
    publish_posts.short_description = 'Publish selected confirmed posts'
