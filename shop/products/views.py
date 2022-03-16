from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import Product, Category
from . import tasks
from django.contrib import messages
from utils import IsUserAdminMixin


# Home page of site that shows products, categories etc.
class Home(View):
    def get(self, request, category_slug=None):
        categories = Category.objects.filter(is_sub=False)
        products = Product.objects.filter(available=True)
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category) 
        return render(request, 'products/home.html', {'products': products, 'categories': categories})


class ProductDetailView(View):
    def get(self, request, slug):
        products = get_object_or_404(Product, slug=slug)
        return render(request, 'products/product_detail.html', {'products': products})


class BucketView(IsUserAdminMixin, View):

    template_name = 'products/bucket.html'

    def get(self, request):
    	objects = tasks.all_bucket_objects_task()
    	return render(request, self.template_name, {'objects': objects})

class BucketDeleteView(IsUserAdminMixin, View):
    
    def get(self, request, key):    
        tasks.delete_object_task.delay(key)
        messages.success(request, 'object will be deleted soon!', 'success')
        return redirect('products:bucket')

class BucketDownloadView(IsUserAdminMixin, View):
    
    def get(self, request, key):    
        tasks.download_object_task.delay(key)
        messages.success(request, 'object will be downloaded soon!', 'success')
        return redirect('products:bucket')