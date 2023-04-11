from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='profile_photos')
