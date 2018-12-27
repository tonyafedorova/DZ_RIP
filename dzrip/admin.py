from django.contrib import admin

# Register your models here.
from .models import customer, PurchaseModel, PictureModel

admin.site.register(customer)
admin.site.register(PurchaseModel)
admin.site.register(PictureModel)