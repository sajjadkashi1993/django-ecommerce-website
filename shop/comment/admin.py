from django.contrib import admin
from .models import Comment
from django.contrib import messages


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    actions = ['delete_selected', 'make_approved', 'make_rejected']
    list_display = ('user', 'nickname','product', 'body', 'status')
    list_editable = ('status',)
    list_filter = ('status', 'product')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    raw_id_fields = ('parent',)
    empty_value_display = '-empty-'
    search_fields = ('comment','product')

    @admin.action(description='Make Approved')
    def make_approved(modeladmin, request, queryset):
        queryset.update(status = 2)
        messages.success(request, "Selected Record(s) Marked as Approved Successfully !!")
    
    @admin.action(description='Make Rejected')
    def make_rejected(modeladmin, request, queryset):
        queryset.update(status = 3)
        messages.success(request, "Selected Record(s) Marked as Rejected Successfully !!")




