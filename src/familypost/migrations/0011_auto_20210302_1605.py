# Generated by Django 3.1.7 on 2021-03-02 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familypost', '0010_auto_20210228_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.CharField(default='name', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default='name', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default='name', max_length=255),
            preserve_default=False,
        ),
    ]
