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



class Doctor (models.Model):
    name = models.CharField(max_length=122)
    date_of_birth = models.DateField()
    email= models.CharField(max_length=122)
    photo = models.ImageField(upload_to='static/docs_img')
    phone= models.CharField(max_length=15)
    DEPT=(
        ('Pediatrician','Pediatrician'),
        ('Gynecologist','Gynecologist'),
        ('Psychiatrist','Psychiatrist'),
        ('Cardiologist','Cardiologist'),
        ('Dermatologist','Dermatologist'),
        ('Endocrinologist','Endocrinologist'),
        ('Gastroenterologist','Gastroenterologist'),
        ('Nephrologist','Nephrologist'),
        ('Ophthalmologist','Ophthalmologist'),
        ('Otolaryngologist','Otolaryngologist'),
        ('Pulmonologist','Pulmonologist'),
        ('Neurologist','Neurologist'),
        ('Oncologist','Oncologist'),
    )
    department = models.CharField(max_length=50, choices=DEPT)
    date_of_join  = models.DateField()

    def __str__(self):
        return self.name
