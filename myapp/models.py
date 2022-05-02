from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name

class Course(models.Model):
    name =models.CharField(max_length=30)    
    students= models.ManyToManyField(Student)

    def __str__(self):
        return self.name


class Streams(models.Model):
    COURSES= (
        ('B.E.','B.E.'),
        ('MTech.','MTech'),
        ('PhD','PhD'),
    )
    name = models.CharField(max_length=100)
    fees= models.FloatField()
    course= models.CharField(max_length=100,choices=COURSES)
    