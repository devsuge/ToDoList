# Generated by Django 3.2 on 2021-05-01 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='file_data',
            field=models.FileField(blank=True, upload_to='uploads/%Y/%m/%d'),
        ),
    ]
