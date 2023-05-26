from django.contrib import admin
from .models import Publisher


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city']
    fieldsets = (
        ('Имя', {
            'fields': ['name'],
            'description': 'имя'
        }),
        ('Все остальное', {
            'fields': ('genre', 'city', 'country', 'is_active'),
            'description': 'Все остальное',
            'classes': ['collapse']
        })
    )


admin.site.register(Publisher, PublisherAdmin)
