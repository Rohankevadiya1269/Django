from django.db import models

# Create your models here.
class UserDetail(models.Model):
    name = models.CharField(max_length = 50)
    emailId = models.EmailField(max_length = 250)
    age = models.IntegerField(max_length = 3)

    def __str__(self):  # this is representation of object
        return f"{self.name}, {self.emailId}, {self.age}"
