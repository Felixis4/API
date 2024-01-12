from django.db import models

class Movies(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    year = models.CharField(max_length=8)
    director = models.CharField(max_length=50)
    studio = models.CharField(max_length=50)
    
