# Generated by Django 4.2.7 on 2023-12-13 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_remove_member_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]