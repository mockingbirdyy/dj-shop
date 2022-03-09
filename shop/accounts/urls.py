from django.urls import path 
from . import views


app_name = 'accounts'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('verify_code/', views.VerifyCodeView.as_view(), name='verify_code'),
    path('verify_code/again/', views.SendVerifyCodeAgain.as_view(), name='verify_code_again'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('user_password_reset/', views.UserPasswordResetView.as_view(), name='user_password_reset'),
    path('user_password_reset_done/', views.UserPasswordResetDoneView.as_view(), name='user_password_reset_done'),
    path('user_password_reset_confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='user_password_reset_confirm'),
    path('user_password_reset_complete/', views.UserPasswordResetCompleteView.as_view(), name='user_password_reset_complete'),

    
]

