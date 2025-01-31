from django.db import models

# Create your models here.

class storeModel(models.Model):
    name=models.CharField(max_length=20)
    company=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()
    expiry=models.DateField()
    picture=models.FileField()
    
    def __str__(self):
        return self.name