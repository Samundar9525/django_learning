from django.db import models

class users(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    gender = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    phone = models.IntegerField()
    salary = models.IntegerField()
    address = models.CharField(max_length=400)


 