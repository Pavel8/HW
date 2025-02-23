from django.db import models

class Jacket(models.Model):
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.brand} - {self.color}"