from django.contrib import admin

# Register your models here.
from .models import CustomerModel, PurchaseModel, PictureModel

admin.site.register(CustomerModel)
admin.site.register(PurchaseModel)
admin.site.register(PictureModel)