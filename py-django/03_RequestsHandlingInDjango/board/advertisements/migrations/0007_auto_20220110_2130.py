# Generated by Django 2.2 on 2022-01-10 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0006_auto_20220107_2155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelTable(
            name='advertisement',
            table='advretisements',
        ),
    ]
