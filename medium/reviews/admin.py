from csv import list_dialects
from django.contrib.auth.models import Group
from django.contrib import admin
from .models import Product, Category, Company, ProductSite, ProductSize, Comment,Image

# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('name',)

# advanced model configuration
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # show more info in Home/Reviews/Products 
    list_display = ('pk','name','content')
    list_filter = ('category',)
    

# admin.site.register(Product,ProductAdmin) <- admin.site.register method
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(ProductSite)
admin.site.register(ProductSize)
admin.site.register(Comment)

# unregister
admin.site.unregister(Group)

# change the title
admin.site.site_header = "Product Review Admin"
