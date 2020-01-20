from django.db import models

# Create your models here.
CHOICES = [
        ('1', 'Sem_1'),
        ('2', 'Sem_2'),
        ('3', 'Sem_3'),
        ('4', 'Sem_4'),
        ('5', 'Sem_5'),
        ('6', 'Sem_6'),
        ('7', 'Sem_7'),
        ('8', 'Sem_8')
]
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    PRN = models.CharField(max_length=10,unique=True,primary_key=True)

class Marks(models.Model):
    PRN = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.CharField(max_length=10, choices=CHOICES, default='1')
    subject1 = models.CharField(max_length=20)
    subject2 = models.CharField(max_length=20)
    subject3 = models.CharField(max_length=20)
    subject4 = models.CharField(max_length=20)  