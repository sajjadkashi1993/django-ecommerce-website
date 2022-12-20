from django.contrib import admin
from .models import Comment

# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname','product', 'created_at', 'status')
    list_editable = ('status',)
    list_filter = ('status', 'product')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    raw_id_fields = ('parent',)
