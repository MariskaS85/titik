# Generated by Django 3.1.6 on 2021-04-16 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
