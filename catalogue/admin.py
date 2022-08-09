from atexit import register
from django.contrib import admin
from .models import Kayak, Photo


class PhotoInline(admin.StackedInline):
    model = Photo


class KayakAdmin(admin.ModelAdmin):
    model = Kayak
    list_display = ['brand', 'model_name', 'material', 'description', 'key_features', 'length', 'width', 'height', 'weight',
                    'load_capacity']
    # list_filter = ['brand', 'material', 'steering', 'paddling', 'is_new', 'in_stock']
    search_fields = ['brand', 'model_name', 'material', 'load_capacity', 'weight']
    inlines = [PhotoInline]
    list_display_links = ['model_name']
    ordering = ['id']


admin.site.register(Kayak, KayakAdmin)
