from django.db import models

# Create your models here.

class daysactivity(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)   
    due_date = models.DateField(null=True, blank=True)  
