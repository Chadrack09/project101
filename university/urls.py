from django.urls import path, include

from university import views

from .views import *

app_name = 'university'

urlpatterns = [
    path('university', views.university, name='university'),
]