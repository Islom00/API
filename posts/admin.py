from django.contrib import admin

from posts.models import PostModel


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "body", "created_at", "updated"]
