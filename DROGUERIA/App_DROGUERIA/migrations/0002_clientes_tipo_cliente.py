# Generated by Django 4.0.6 on 2022-08-12 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_DROGUERIA', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='tipo_Cliente',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
