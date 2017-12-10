# Generated by Django 2.0 on 2017-12-10 14:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurace', '0002_auto_20171210_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='contact',
            field=models.CharField(default='+420123123123', max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dish',
            name='basePrice',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]