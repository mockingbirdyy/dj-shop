from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # include url file in your app and namespace is your app name
    path('', include('accounts.urls', namespace='accounts')),
    path('', include('products.urls', namespace='products')),

]       
