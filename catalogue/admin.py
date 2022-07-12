from atexit import register
from django.contrib import admin
from .models import Kayak, Photo

class PhotoInline(admin.StackedInline):
    model = Photo

class KayakAdmin(admin.ModelAdmin):
    model = Kayak
    list_display = ['brand', 'model', 'build', 'description', 'length', 'width', 'height', 'weight', 'load_capacity']
    list_filter = ['brand', 'build', 'steering', 'paddling', 'is_new', 'in_stock']
    search_fields = ['brand', 'model', 'build', 'load_capacity', 'weight']
    inlines = [PhotoInline]

admin.site.register(Kayak, KayakAdmin)