from django.contrib import admin
from .models import News, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'actual']
    inlines = [CommentInline]
    list_filter = ['actual']
    list_editable = ['actual']
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'actual')
        }),
        ('Описание', {
            'fields': ['description'],
            'classes': ['collapse']
        })
    )
    actions = ['make_actual', 'make_no_actual']

    def make_actual(self, request, queryset):
        queryset.update(actual=True)

    def make_no_actual(self, request, queryset):
        queryset.update(actual=False)

    make_actual.short_description = 'активно'
    make_no_actual.short_description = 'неактивно'


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'modified_text_comment', 'administration']
    list_display_links = ['modified_text_comment']
    list_filter = ['user_name']
    actions = ['admin_as_delete']

    def modified_text_comment(self, obj):
        return obj.text[:15]

    def admin_as_delete(self, request, queryset):
        queryset.update(administration='d')

    admin_as_delete.short_description = 'Удалено администратором'
    modified_text_comment.short_description = 'text'


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
