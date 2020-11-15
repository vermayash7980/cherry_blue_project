from django.db import models
from home.models import Doctor

# Create your models here.
class patient (models.Model):
    name=models.CharField( max_length=122)
    address=models.TextField()
    date_of_birth=models.DateField()
    date_of_admit=models.DateField()
    contact_no=models.CharField( max_length=15)
    blood_grp=models.CharField( max_length=5)
    depar=Doctor.DEPT
    dept=models.CharField( max_length=50,choices=depar)
    description=models.TextField()