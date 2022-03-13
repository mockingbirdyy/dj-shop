from django.urls import path, include
from . import views

app_name = "products"


bucket_urls = [

    path("", views.BucketView.as_view(), name="bucket"),
    path("delete_obj/<str:key>/", views.BucketDeleteView.as_view(), name="delete_object"),
    path("download_obj/<str:key>/", views.BucketDownloadView.as_view(), name="download_object"),

]
urlpatterns = [
    
    path("", views.Home.as_view(), name="home"),
    path("bucket/", include(bucket_urls)),
    path("products/<slug:slug>/", views.ProductDetailView.as_view(), name="product_detail"),

] 