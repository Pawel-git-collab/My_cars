from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Car


@admin.register(Car)
class CarAdmin(SimpleHistoryAdmin):
    list_display = ['cars', 'speed', 'price', 'mileage', 'created', 'image_car', 'thumbnail_preview']
    history_list_display = ['cars']
    search_fields = ['cars']
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'thumbnail preview'
    thumbnail_preview.allow_tags = True
