# Generated by Django 2.1.2 on 2018-11-02 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_auto_20181102_0133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perrito',
            old_name='ESTADOS',
            new_name='Estado',
        ),
    ]
