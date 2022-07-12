from atexit import register
from django.contrib import admin
from .models import Kayak, Feature

class FeatureInline(admin.StackedInline):
    model = Feature
admin.site.register(Feature)

class KayakAdmin(admin.ModelAdmin):
    model = Kayak
    list_display = ['brand', 'model', 'build', 'description', 'length', 'width', 'height', 'weight', 'load_capacity']
    list_filter = ['brand', 'build', 'steering', 'paddling', 'is_new', 'in_stock']
    inlines = (Feature,)

admin.site.register(Kayak)