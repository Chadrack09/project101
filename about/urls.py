from django.urls import path, include

from about import views

from .views import about

app_name = 'about'

urlpatterns = [
    path('about', views.about, name='about'),
]