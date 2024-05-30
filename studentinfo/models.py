from django.db import models

# Create your models here.
class Student(models.Model):
    MAJOR_CHOICES = [
        ('CSIT','Bsc.Csit'),
        ('BIT','Bit'),
        ('BCA','Bca'),
        ('CS', 'Computer Science'),
        ('EE', 'Electrical Engineering'),
        ('CE', 'Civil Engineering'),
        ('BIO', 'Biology'),
        ('PHY', 'Physics'),
        
    ]
    
    LEVEL=[
        ('+2','+2 graduate'),
        ('BACHELOR','Bachelor'),
        ('MASTER','master'),
        ]
    
    student_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age = models.IntegerField()
    email_id=models.EmailField( max_length=30)
    level=models.CharField(max_length=50,choices=LEVEL,default=1)
    phone=models.CharField(max_length=10,blank=True,null=True)
    address = models.CharField(max_length=255)
    grade = models.CharField(max_length=10)
    major = models.CharField(max_length=50, choices=MAJOR_CHOICES)

    def __str__(self):
        return f"{self.first_name} ({self.major} - Grade: {self.grade})"