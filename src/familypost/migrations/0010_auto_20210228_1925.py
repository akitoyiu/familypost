# Generated by Django 3.1.7 on 2021-02-28 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familypost', '0009_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='ig_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='www_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
