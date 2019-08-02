from django.shortcuts import render

#import University model
from .models import UniversityView
# Create your views here.

def university(request):
    context = {
        'university':UniversityView.objects.all()
    }

    return render(request, 'university/university.html', context)