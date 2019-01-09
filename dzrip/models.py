from django.db import models
from django.contrib.auth.models import User, AbstractUser, UserManager
from django.utils.translation import ugettext_lazy as _


class customer(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True,
                               default='avatars/111_XTdrxrR.jpg',
                               verbose_name='Аватар')
    description = models.CharField(max_length=255, verbose_name='О себе', blank=True, null=True)
    objects = UserManager()

    class Meta:
        db_table = 'Customer'
        verbose_name = _('Профиль пользователей')
        verbose_name_plural = _('Профили пользователей')


customer._meta.get_field('username').verbose_name = 'Имя пользователя'


class Picture(models.Model):
    name = models.CharField(max_length=80, verbose_name='Название')
    description = models.CharField(max_length=255, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Стоимость')
    author = models.CharField(max_length=100, verbose_name='Автор', default='Не указан')
    like = models.ManyToManyField(customer, verbose_name='Лайки', default=0, blank=True)
    image = models.ImageField(upload_to='pics/', blank=True, null=True,
                              default='pics/111.jpg',
                              verbose_name='Изображение')

    def total_likes(self):
        return self.like.count()


    class Meta:
        db_table = 'Picture'
        verbose_name = _('Картина')
        verbose_name_plural = _('Картины')
