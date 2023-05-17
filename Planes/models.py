from django.contrib.gis.db import models


class Plan(models.Model):
    nombre =  models.TextField()
    def __str__(self):
        return f"Plan {self.nombre}"


