from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# 2 Models
# Products Category
class ParentCategory(models.Model):
    parent_cat = models.CharField(max_length=100)
    parent_cat_slug = AutoSlugField(populate_from='parent_cat', unique=True, null=True, default=None)

    class Meta:
        verbose_name_plural = 'Parent Categories'
    
    def __str__(self):
        return self.parent_cat

# work on cat is_active
CHILD_CATEGORY_STATUE_CHOICE = (
    ('True','Active'),
    ('False','Unactive'),
)
    
class ChildCategory(models.Model):
    parent_category = models.ForeignKey('ParentCategory', on_delete=models.CASCADE)
    child_cat = models.CharField(max_length=100)
    child_cat_slug = AutoSlugField(populate_from='child_cat', unique=True, null=True, default=None)
    is_active = models.CharField(max_length=100, choices=CHILD_CATEGORY_STATUE_CHOICE, default='False')

    class Meta:
        verbose_name_plural = 'Child Categories'

    def __str__(self):
        return self.child_cat

# CustomerAddress
class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class City(models.Model):
    state = models.ForeignKey('State', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Cities'
        ordering = ["name"]

    def __str__(self):
        return self.name

class CustomerAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    state = models.ForeignKey('State', on_delete=models.CASCADE) # ? 
    city = models.ForeignKey('City', on_delete=models.CASCADE)   # ?
    address = models.CharField(max_length=200)
    Zipcode = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Customers Address'
    
    def __str__(self):
        return str(self.id)

# ProductBrand
class Brand(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey('ParentCategory', on_delete=models.CASCADE, null=True, default=None)
    child_category = models.ForeignKey('ChildCategory', on_delete=models.CASCADE, null=True, default=None)

    class Meta:
        verbose_name_plural = 'Products Brand'
    
    def __str__(self):
        return str(self.name)

# Products
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    parent_category = models.ForeignKey('ParentCategory', on_delete=models.CASCADE)
    child_category = models.ForeignKey('ChildCategory', on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='product_image')

    def __str__(self):
        return str(self.id)

# Carts
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    # for single product price according quantity # 12
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

# Place Order
# Accepted, Packed, On The Way, Delivered, Cancel
class OrderStatus(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Order Status'

    def __str__(self):
        return self.name

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_address = models.ForeignKey('CustomerAddress', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    order_status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name_plural = 'Orders Placed'

    def __str__(self):
        return str(self.id)

    # for single product price according quantity # 12
    @property
    def total_qty_cost(self):
        return self.quantity * self.product.discounted_price