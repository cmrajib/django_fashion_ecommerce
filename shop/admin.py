from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

# Register your models here.
from shop.models import Product, Category, ProductColor, ProductSize, Subcategory, Brand


class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('category_name',), }


class SubcategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('subcategory_name',), }

class BrandAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('brand_name',), }

class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.image.url))

    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'title', 'stock','price','discountprice','DateArrived')
    list_display_links = ('id','thumbnail', 'title')
    list_filter = ['title']
    # list_editable = ('is_published',)
    search_fields =('user', 'title')
    list_per_page = 10

    prepopulated_fields = {'slug': ('title',), }

admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductColor)
admin.site.register(ProductSize)
