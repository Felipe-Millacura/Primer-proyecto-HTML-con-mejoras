# Generated by Django 2.1.2 on 2018-11-04 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0014_auto_20181104_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perrito',
            name='Foto',
            field=models.ImageField(upload_to='Media'),
        ),
    ]