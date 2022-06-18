from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length= 200, unique= True)
    text = models.TextField(unique= True)
    author = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    created_date = models.DateTimeField(default= datetime.now)
    published_date = models.DateTimeField(default= datetime.now)