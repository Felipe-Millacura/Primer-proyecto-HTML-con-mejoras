# Generated by Django 2.1.2 on 2018-11-04 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0012_auto_20181104_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perrito',
            name='Foto',
            field=models.ImageField(null=True, upload_to='Media'),
        ),
    ]