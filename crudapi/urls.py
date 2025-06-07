from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path




urlpatterns = [
    
    path('register/', views.register, name='register'),
    path('profile/complete/', views.profile_complete, name='profile_complete'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name="dashboard"),
      path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('students/', views.student_list, name='student_list'),
    path('students/detail/', views.student_detail, name='student_detail'),
    path('experts/', views.expert_list, name='expert_list'),
    path('experts/detail/', views.expert_detail, name='expert_detail'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/edit/', views.course_edit, name='course_edit'),
    path('subscriptions/', views.subscription_settings, name='subscription_settings'),
    path('feedbacks/', views.feedback_review, name='feedback_review'),
     
     
   
]
