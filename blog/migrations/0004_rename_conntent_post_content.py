# Generated by Django 3.2.5 on 2023-03-21 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230319_2009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='conntent',
            new_name='content',
        ),
    ]
