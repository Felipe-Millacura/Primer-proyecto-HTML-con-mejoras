# Generated by Django 2.1.2 on 2018-11-02 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0009_perrito_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perrito',
            name='Foto',
            field=models.ImageField(default=True, upload_to='Media'),
        ),
    ]
