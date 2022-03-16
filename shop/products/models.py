from django.db import models
from django.shortcuts import reverse

class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_category_related', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=40, unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:product_category", args=[self.slug])
    
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=60)
    slug = models.SlugField(max_length=40, unique=True)
    category = models.ManyToManyField(Category, related_name='product_category_related')
    # pip install pillow for working with images in django
    image = models.ImageField()
    description = models.TextField(max_length=10000)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)	
    country	= models.CharField(max_length=40)
    language = models.CharField(max_length=30)
    genre = models.CharField(max_length=40)	
    published = models.DateField()		
    pages = models.SmallIntegerField()	
    awards = models.CharField(max_length=400, null=True, blank=True)


    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} - {self.author} - {self.category} - {self.price}  - available:{self.available}'
    

    def get_absolute_url(self):
        return reverse("products:product_detail", args=[self.slug])
    