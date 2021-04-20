# Generated by Django 3.1.7 on 2021-03-18 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familypost', '0019_auto_20210318_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='media',
        ),
        migrations.AddField(
            model_name='post',
            name='postmedia',
            field=models.ManyToManyField(blank=True, null=True, related_name='postmedia', to='familypost.PostMedia'),
        ),
    ]
