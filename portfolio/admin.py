from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Tag, Project, Post


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'featured', 'order', 'created_at']
    list_editable = ['status', 'featured', 'order']
    list_filter = ['status', 'featured']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['tags']
    search_fields = ['title', 'tagline']


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = ['title', 'published', 'featured', 'read_time_minutes', 'published_at']
    list_editable = ['published', 'featured']
    list_filter = ['published', 'featured']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['tags']
    search_fields = ['title', 'excerpt']
