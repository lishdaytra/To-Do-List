# Generated by Django 4.2.7 on 2023-11-10 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='date_end',
            new_name='created_end',
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
