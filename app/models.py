from django.db import models

# Create your models here.
class UserCsv(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, default="example@example.com")
