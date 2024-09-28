from django.contrib import admin
from .models import Announcement, Profile

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'slug', 'price',
                    'author', 'publish', 'description',
                    'company', 'experience', 'address']
    search_fields = ['title', 'company', 'body']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ['user', 'age']
    raw_id_fields = ['user']