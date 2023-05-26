# Generated by Django 2.2 on 2022-04-06 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0005_entry_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='file',
        ),
        migrations.CreateModel(
            name='PicSecond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='')),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_blog.Entry')),
            ],
        ),
        migrations.CreateModel(
            name='PicFirst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='')),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_blog.Entry')),
            ],
        ),
    ]
