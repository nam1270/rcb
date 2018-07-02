from django.db import models
import uuid
import random

class Resident(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cottage = models.ForeignKey('Cottage',on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.last_name

class Cottage(models.Model):
    cottage_number = models.CharField(max_length=5)
    unique_key = models.IntegerField(default='00000',primary_key=True)
    RENT_STATUS = (
        ('p','Paid'),
        ('d','Due'),

    )
    payment_status = models.CharField(max_length=1,choices=RENT_STATUS, blank=True, default='d',help_text='Rent Status')
    def __str__(self):
        return self.cottage_number