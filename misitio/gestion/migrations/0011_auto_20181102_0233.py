# Generated by Django 2.1.2 on 2018-11-02 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0010_auto_20181102_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perrito',
            name='Foto',
            field=models.ImageField(upload_to='Media'),
        ),
    ]