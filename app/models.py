from django.contrib.gis.db import models
from Planes.models import Plan




class Cobertura(models.Model):
    color = models.CharField(blank=True, null=True, max_length=100)
    location = models.GeometryField(blank=False)
    planes = models.ManyToManyField(Plan)


    def __str__(self):
        return f"{self.color}"
    

    

        


