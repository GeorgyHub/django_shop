from django.contrib import admin
from shop_app.models import Items, Categories, Brands

# Register your models here.
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'ItemName', 'ItemPhoto', 'ItemCategories', 'ItemPrice', 'ItemBacketCount', 'ItemText', 'Item')
    list_display_links = ('id', 'ItemName')
    search_fields = ('id', 'ItemName')

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'ItemCategories')
    list_display_links = ('id', 'ItemCategories')
    search_fields = ('id', 'ItemCategories')

class BrandsAdmin(admin.ModelAdmin):
    list_display = ('id', 'NameBrand', 'ImageBrand')
    list_display_links = ('id', 'NameBrand')
    search_fields = ('id', 'NameBrand')

admin.site.register(Items, ItemsAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Brands, BrandsAdmin)