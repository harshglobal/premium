from django.urls import path, include
from . import views


urlpatterns = [
  
    path('signup/', views.signup, name='signup'),
 

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
 

    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password_validate/<uidb64>/<token>/', views.reset_password_validate, name='reset_password_validate'),
    path('reset_password/', views.reset_password, name='reset_password'),



]