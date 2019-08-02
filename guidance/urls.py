from django.urls import path, include

from guidance import views
from .views import *

app_name = 'guidance'

urlpatterns = [
    path('guidance', views.guidance, name='guidance'),
]