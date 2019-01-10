from django.contrib import admin

from .models import customer, Picture


class PictureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'image', 'author')
    search_fields = ('name', 'author')


admin.site.register(customer)
admin.site.register(Picture, PictureAdmin)