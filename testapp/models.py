from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()
# Create your models here.
class Post(models.Model):
    title=models.CharField( max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now()) 
    owner = models.ForeignKey(User,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title
    