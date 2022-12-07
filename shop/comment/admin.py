from django.contrib import admin
from .models import Comment

# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname', 'body', 'created_at', 'status')
    list_editable = ['status']
