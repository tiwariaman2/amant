# Generated by Django 4.2.1 on 2023-08-29 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employlist',
            old_name='f_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='employlist',
            name='l_name',
        ),
        migrations.AddField(
            model_name='employlist',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
