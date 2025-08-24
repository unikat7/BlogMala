from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    image=models.ImageField(upload_to="images")
    title=models.CharField(max_length=255)
    subtitle=models.CharField(max_length=255)
    description=models.TextField()
    author_id=models.ForeignKey(User,on_delete=models.CASCADE)
