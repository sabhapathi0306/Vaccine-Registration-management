
from django.db import models
from django.db.models.expressions import F

# Create your models here.
class details(models.Model):
    Name = models.CharField(max_length=200,null=False)
    Aadhar_number = models.CharField(max_length = 20 ,null=False)
    Phone_number = models.CharField(max_length=20,null=False)
    Vaccine = models.CharField(max_length=50)
    Gender = models.TextField(max_length=20)
    Age = models.IntegerField()
    Date =models.DateField(null=False)
    doseage = models.CharField(max_length=100)
    Group = models.CharField(max_length=50,null=False)
    Disability = models.CharField(max_length=50)
    State = models.CharField(max_length=100,null=True)
    District = models.CharField(max_length=100,null=True)
    Aadress = models.TextField(max_length=250,null=True)
    Pin = models.CharField(max_length=10,null=False)
    Ref_token = models.CharField(max_length=8,null=False)
    Status = models.CharField(max_length=50,null=True)
    Rec_Date = models.DateField(null=True)
    class Meta:
        db_table = 'vacc_details'