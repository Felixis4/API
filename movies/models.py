from django.db import models

class Movies(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    year = models.IntegerField(blank=False, null=False)
    studio = models.CharField(max_length=50)
    
