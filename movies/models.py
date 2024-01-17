from django.db import models

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)

class Directors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class Movies(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    year = models.IntegerField(blank=False, null=False)
    director = models.ForeignKey(Directors,on_delete=models.CASCADE)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    studio = models.CharField(max_length=50)
    





    
    
    


    
