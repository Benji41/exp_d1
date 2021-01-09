from django.db import models

# Create your models here.
class Cat(models.Model):
    catName =models.CharField(max_length=10,unique=True)
    def __str__(self):
        return self.catName

class Owner(models.Model):
    ownName =models.CharField(max_length=15,unique=True)
    ownCat = models.ForeignKey(Cat,on_delete=models.CASCADE)
    ownPhoto =models.URLField(unique=True)
    def __str__(self):
        return self.ownName

class AccessRecord(models.Model):
    arName = models.ForeignKey(Owner,on_delete=models.CASCADE)
    arDate = models.DateField()

    def __str__(self):
        return self.arDate
