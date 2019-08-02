from django.shortcuts import render

from .models import *
# Create your views here.

def guidance(request):
    context = {
        'university': GuidanceView.objects.all()
    }
    return render(request, 'guidance/guidance.html', context)