from django.contrib import admin

from products.forms import ColorAdminForm
from products.models import CategoryModel, TagModel, SizeModel, BrandModel, ProductModel, ColourModel, ProductImageModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(ColourModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
    list_filter = ('created_at',)
    form = ColorAdminForm


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ('name',)
    list_filter = ('created_at',)


class ProductImageModelAdmin(admin.StackedInline):
    model = ProductImageModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("name", 'price', )
    search_fields = ('name', 'short_description', )
    list_filter = ('created_at',)
    inlines = [ProductImageModelAdmin]
    readonly_fields = ('real_price', )


