from django.shortcuts import render

from .models import Contact
# Create your views here.

#creating contact view using function based views

def contact(request):
    context = {
        'contacts': Contact.objects.all()
    }
    return render(request, 'contact/contact.html', context)
