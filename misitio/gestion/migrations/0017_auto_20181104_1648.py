# Generated by Django 2.1.2 on 2018-11-04 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0016_auto_20181104_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perrito',
            name='Foto',
            field=models.ImageField(blank=True, default=None, upload_to='Media'),
        ),
    ]