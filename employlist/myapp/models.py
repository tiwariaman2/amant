from django.db import models

# Create your models here.
class employlist(models.Model):
    name=models.CharField(max_length=200)
    phone=models.IntegerField(default=0)
    email=models.EmailField(max_length=200)
    def __str__(self):
        return self.name

