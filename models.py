from django.db import models
from telnetlib import STATUS

class homerental21F22072(models.Model):
    Typeofhome = models.CharField(max_length=30)
    RentDuration = models.CharField(max_length=30)
    BHK = models.CharField(max_length=30)

    def __str__(self):
        return self.homerental21F22072
