from django.db import models


class CustomerModel(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)



class PictureModel(models.Model):
    picname = models.CharField(max_length=30)
    description = models.CharField(max_length=255)


class PurchaseModel(models.Model):
    idcustomer = models.IntegerField()
    idpicture = models.IntegerField()

