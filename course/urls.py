from django.urls import path
from .views import course_detail, Home
urlpatterns = [
    path('', Home,name='home'),
    path('course/<slug>', course_detail,name='course_detail'),

   

]