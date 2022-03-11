from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Product

# home page of site that shows products, categories  etc.


class Home(View):
    def get(self, request):
    	products = Product.objects.filter(available=True)
    	return render(request, 'products/home.html', {'products': products})


class ProductDetailView(View):
    def get(self, request, slug):
    	products = get_object_or_404(Product, slug=slug)
    	return render(request, 'products/product_detail.html', {'products': products})
