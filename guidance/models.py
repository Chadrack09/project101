from django.db import models
from django.contrib.auth import get_user_model

#CREATE global variable user
User = get_user_model()
# Create your models here.

class GuidanceView(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
   # post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"

        