from django.urls import path 
from . import views


app_name = 'accounts'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('verify_code/', views.VerifyCodeView.as_view(), name='verify_code'),
    path('verify_code/again/', views.SendVerifyCodeAgain.as_view(), name='verify_code_again'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]

