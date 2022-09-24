from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

class ParentCategory(models.Model):
    parent_cat = models.CharField(max_length=100)
    parent_cat_slug = AutoSlugField(populate_from='parent_cat', unique=True, null=True, default=None)

    class Meta:
        verbose_name_plural = 'Parent Categories'
    
    def __str__(self):
        return self.parent_cat

CHILD_CATEGORY_STATUE_CHOICE = (
    (1,'Active')
)
class ChildCategory(models.Model):
    parent_category = models.ForeignKey('ParentCategory', on_delete=models.CASCADE)
    child_cat = models.CharField(max_length=100)
    child_cat_slug = AutoSlugField(populate_from='child_cat', unique=True, null=True, default=None)
    is_active = models.CharField(max_length=100, default=0)

    class Meta:
        verbose_name_plural = 'Child Categories'

    def __str__(self):
        return self.child_cat

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    parent_category = models.ForeignKey('ParentCategory', on_delete=models.CASCADE)
    child_category = models.ForeignKey('ChildCategory', on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='product_image')

    def __str__(self):
        return str(self.id)
