# Generated by Django 3.1 on 2020-08-23 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200823_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
    ]
