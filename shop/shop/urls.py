from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # include url file in your app and namespace is your app name
    path('', include('accounts.urls', namespace='accounts')),
    path('', include('products.urls', namespace='products')),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)     
