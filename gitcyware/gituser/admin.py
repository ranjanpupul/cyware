from django.contrib import admin
from .models import GitUser
# Register your models here.

class GitUserAdmin(admin.ModelAdmin):
    list_display = ['login', 'user_id','image_tag', 'followers_url','site_admin', 'repos_url',]
    list_filter = ['login', 'user_id', 'followers_url', 'followers_url', 'repos_url']
    search_fields = ['login', 'user_id', 'followers_url',]
    fields = ('login', 'user_id', 'image', 'image_tag', 'followers_url', 'site_admin', 'repos_url',)
    ordering = ['updated_on']
    readonly_fields = ('image_tag',)


admin.site.register(GitUser, GitUserAdmin)