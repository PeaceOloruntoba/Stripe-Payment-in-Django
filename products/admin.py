from django.contrib import admin
from .models import Product
from .models import Product, Price

# Register your models here

class PriceInlineAdmin(admin.TabularInline):
    model = Price
    extra = 0
class ProductAdmin(admin.ModelAdmin):
    inlines = [PriceInlineAdmin]
admin.site.register(Product, ProductAdmin)
