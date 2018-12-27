from django.db import models
from django.contrib.auth.models import User, AbstractUser, UserManager
from django.utils.translation import ugettext_lazy as _


# class CustomerModel(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
#     name = models.CharField(max_length=30)
#     surname = models.CharField(max_length=30)
#     city = models.CharField(max_length=100, default='')
#     phone = models.IntegerField(default=0)

#     def __str__(self):
#         return self.user.username
#
#
# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = CustomerModel.objects.create(user=kwargs['instane'])
# post_save.connect(create_profile, sender=User)


class customer(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True,
                               default='avatars/default_avatar.png',
                               verbose_name='Аватар')
    description = models.CharField(max_length=255, verbose_name='О себе', blank=True, null=True)
    objects = UserManager()

    class Meta:
        db_table = 'Customer'
        verbose_name = _('Профиль пользователей')
        verbose_name_plural = _('Профили пользователей')


customer._meta.get_field('username').verbose_name = 'Имя пользователя'


class PictureModel(models.Model):
    picname = models.CharField(max_length=30)
    description = models.CharField(max_length=255)


class PurchaseModel(models.Model):
    idcustomer = models.IntegerField()
    idpicture = models.IntegerField()
