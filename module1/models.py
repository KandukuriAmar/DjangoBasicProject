from django.db import models
class Amar(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    phonenumber = models.IntegerField()
    class Meta:
        db_table="Amar"
# Create your models here.

class Feed(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    comment = models.CharField(max_length=250)
    class Meta:
        db_table="Feed"