from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
	photo = models.ImageField(upload_to="images")
	user = models.ForeignKey(User, on_delete=models.CASCADE ,blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)
 
class About(models.Model):
    fullName = models.TextField(max_length=40,null=True)
    about = models.TextField(max_length=500,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)