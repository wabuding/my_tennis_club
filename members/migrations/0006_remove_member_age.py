# Generated by Django 4.2.7 on 2023-12-13 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_member_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='age',
        ),
    ]
