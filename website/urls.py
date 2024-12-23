from django.urls import path
from .views import *

app_name = 'website'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('courses/', courses, name='courses'), 
    path('courses/<str:data>/', course_detail, name='course_detail'), 
]