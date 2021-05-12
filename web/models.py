from django.db import models

# Create your models here.

class Member(models.Model):
    sno=models.CharField(max_length=10)
    resumeid=models.CharField(max_length=30,primary_key=True)
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    otp=models.CharField(max_length=30)
    Attend = models.CharField(max_length=30)




    '''def __str__(self):
        return self.resumeid + " " + self.name'''