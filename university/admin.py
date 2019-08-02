from django.contrib import admin

#importing the models to display on the Admin panel
from .models import UniversityView
# Register your models here.

admin.site.register(UniversityView)
