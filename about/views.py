from django.shortcuts import render


#import about us model fom models
from .models import About
# Create your views here.

#creating about us view

def about(request):
    context = {
        'about': About.objects.all()
    }

    return render(request, 'about/about.html')