from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from .views import create_payment_intent




urlpatterns = [
    
    path('register/', views.register, name='register'),
    path('profile/complete/', views.profile_complete, name='profile_complete'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('product/<int:pk>/', views.product, name='product'),
    path('', views.dashboard, name="dashboard"),
    path('create-payment-intent/', views.create_payment_intent, name='create-payment-intent'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
     

   
]
