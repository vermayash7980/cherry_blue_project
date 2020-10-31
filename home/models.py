from django.db import models

# Create your models here.
class Contact_Us(models.Model):
    name = models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    phone= models.CharField(max_length=15)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    