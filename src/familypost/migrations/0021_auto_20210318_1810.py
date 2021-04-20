# Generated by Django 3.1.7 on 2021-03-18 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familypost', '0020_auto_20210318_1751'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmedia',
            options={'verbose_name_plural': 'PostMedias'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='postmedia',
        ),
        migrations.AddField(
            model_name='post',
            name='postmedias',
            field=models.ManyToManyField(blank=True, null=True, related_name='postmedias', to='familypost.PostMedia'),
        ),
    ]
