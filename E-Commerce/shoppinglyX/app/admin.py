from django.contrib import admin
from . import models as mymodel
from django.utils.html import format_html
from django.urls import reverse

@admin.register(mymodel.ParentCategory)
class ParentCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'parent_cat', 'parent_cat_slug']

@admin.register(mymodel.ChildCategory)
class ChildCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'parent_category_id', 'child_cat', 'child_cat_slug', 'is_active']

@admin.register(mymodel.State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(mymodel.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'state_id', 'name']

@admin.register(mymodel.CustomerAddress)
class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'name', 'state', 'city', 'address', 'Zipcode']

@admin.register(mymodel.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent_category_id', 'child_category_id']

@admin.register(mymodel.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price', 'description', 'brand_id', 'parent_category_id', 'child_category_id', 'product_image']

@admin.register(mymodel.Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'product_id', 'quantity']

@admin.register(mymodel.OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(mymodel.OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'customer_address_id', 'customer_info', 'product_id', 'product_info', 'quantity', 'ordered_date', 'order_status']

    # 16
    def customer_info(self, obj):
        link = reverse("admin:app_customeraddress_change", args=[obj.customer_address.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer_address.name)
    
    def product_info(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)
