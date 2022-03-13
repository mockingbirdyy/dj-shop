from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import Product
from . import tasks
from django.contrib import messages
# home page of site that shows products, categories  etc.


class Home(View):
    def get(self, request):
        products = Product.objects.filter(available=True)
        return render(request, 'products/home.html', {'products': products})


class ProductDetailView(View):
    def get(self, request, slug):
        products = get_object_or_404(Product, slug=slug)
        return render(request, 'products/product_detail.html', {'products': products})


class BucketView(View):

    template_name = 'products/bucket.html'

    def get(self, request):
    	objects = tasks.all_bucket_objects_task()
    	return render(request, self.template_name, {'objects': objects})

class BucketDeleteView(View):
    
    def get(self, request, key):    
        tasks.delete_object_task.delay(key)
        messages.success(request, 'object will be deleted soon!', 'success')
        return redirect('products:bucket')

class BucketDownloadView(View):
    
    def get(self, request, key):    
        tasks.download_object_task.delay(key)
        messages.success(request, 'object will be downloaded soon!', 'success')
        return redirect('products:bucket')