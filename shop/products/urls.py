from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("products/<slug:slug>/", views.ProductDetailView.as_view(), name="product_detail"),


] 