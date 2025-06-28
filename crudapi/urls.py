from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from .views import create_payment_intent
from .views import stripe_webhook



urlpatterns = [
    
    path('register/', views.register, name='register'),
    path('profile/complete/', views.profile_complete, name='profile_complete'),
    path('profile/show/', views.profile_show, name="profile_show"), 
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('logout/',views.logout, name='logout'),
    path('product/<int:pk>/', views.product, name='product'),
    path('', views.dashboard, name="dashboard"),
    path('create-payment-intent/', views.create_payment_intent, name='create-payment-intent'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('subscription_success/', views.subscription_success, name='subscription_success'),
    path('about/', views.about, name='about'),
    path('stripe/webhook/', stripe_webhook, name='stripe-webhook'),
    path('subscribe/cancel/', views.subscription_cancel, name='subscription_cancel'),
]
