from django.db import models

#import reverse for absolute url
from django.urls import reverse

#import file validation module
from .validators import image_validation_extension
#South African Provinces
PROVINCES =(
    ('Northern Cape', 'Northern Cape'),
    ('Eastern Cape', 'Eastern Cape'),
    ('Free State', 'Free State'),
    ('Western Cape', 'Western Cape'),
    ('Limpopo', 'Limpopo'),
    ('North West', 'North West'),
    ('KwaZulu-Natal', 'KwaZulu-Natal'),
    ('Mpumalanga', 'Mpumalanga'),
    ('Gauteng', 'Gauteng')
)
# Create your models here.


class UniversityView(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='university/logo/', validators=[image_validation_extension])
    update = models.DateTimeField(auto_now_add=True)
    province = models.CharField(choices=PROVINCES, max_length=244)
    physical_address = models.TextField()

    def get_absolute_url(self):
        return reverse('university:university.html')

    def __str__(self):
        return f"{self.name}"
class Faculty(models.Model):
    name = models.CharField(max_length=255)
    school_or_department = models.CharField(max_length=255)

class Contact(models.Model):
    tel = models.IntegerField()
    emai = models.EmailField()
    website = models.CharField(max_length=255)
class AdmissionRequirement(models.Model):
    subject = models.CharField(max_length=255)