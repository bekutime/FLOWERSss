from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline

from core.models import Product, Sort, Height, ObjectImage

admin.site.register(Sort)
admin.site.register(Height)


class ImageAdminInline(TabularInline):
    extra = 1
    model = ObjectImage


@admin.register(Product)
class ProductModelAdmin(ModelAdmin):
    inlines = (ImageAdminInline,)

    fields = ('name', 'photo', 'price',
              'description', 'color',
              'sum', 'height')