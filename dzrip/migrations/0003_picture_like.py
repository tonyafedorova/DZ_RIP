# Generated by Django 2.1.3 on 2019-01-09 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dzrip', '0002_auto_20190107_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='like',
            field=models.IntegerField(default=0, verbose_name='Лайки'),
        ),
    ]
