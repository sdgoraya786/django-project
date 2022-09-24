from django.contrib import admin
from . import models as mymodel
from .forms import ProductForm
# Register your models here.

@admin.register(mymodel.ParentCategory)
class ParentCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'parent_cat', 'parent_cat_slug']

@admin.register(mymodel.ChildCategory)
class ChildCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'parent_category_id', 'child_cat', 'child_cat_slug']

@admin.register(mymodel.Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ['id', 'title', 'selling_price', 'discounted_price', 'description', 'brand', 'parent_category_id', 'child_category_id', 'product_image']

    class Media:
        js = (
            'app/js/chained-area.js',
        )