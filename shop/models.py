from django.db import models

# Create your models here.
from UserRegistration.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=150)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def category_count(self):
        return self.subcategory.all().count()

class Subcategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='subcategory')
    subcategory_name = models.CharField(max_length=150)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.subcategory_name

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

    def subcategory_count(self):
        return self.product.all().count()





class Brand(models.Model):
    brand_name = models.CharField(max_length=150)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.brand_name

class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE, related_name='product')
    title = models.CharField(max_length=150)
    content = models.TextField()
    longcontent = models.TextField()
    price = models.FloatField(default=0.0)
    discountprice = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0,blank=True)
    hit = models.PositiveIntegerField(default=0)
    image = models.ImageField(blank=True, null=True, upload_to='uploads/')
    shipping = models.CharField(max_length=50, default='1 day shipping. Free pickup')

    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='brand')
    DateArrived = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True)
    deals_of_the_week = models.BooleanField(default=False)


    Checking = models.CharField(max_length=30, blank=True)
    Freshness = models.CharField(max_length=50, blank=True)
    packeting = models.CharField(max_length=50, blank=True)
    each_box_contains = models.CharField(max_length=10, blank=True)


    def __str__(self):
        return self.title

class ProductSize(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='size')
    weight = models.CharField(max_length=50)
    height = models.CharField(max_length=10, blank=True)
    width = models.CharField(max_length=10, blank=True)
    depth = models.CharField(max_length=10, blank=True)

    class Meta:
        verbose_name = 'ProductSize'
        verbose_name_plural = 'ProductSize'

    def __str__(self):
        return self.product.title

class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='color')
    color = models.CharField(max_length=40,blank=True)
    quality = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'ProductColor'
        verbose_name_plural = 'ProductColor'

    def __str__(self):
        return self.product.title

class comment(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='product')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    content = models.TextField(blank=True)
    rating = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.product.title