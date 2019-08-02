import os

def image_validation_extension(value):
    from django.core.exceptions import ValidationError
    img_extension = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    if not img_extension.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.') 
