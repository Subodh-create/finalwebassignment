# Generated by Django 3.1 on 2020-08-25 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_appointment_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='ap', verbose_name='Picture your message'),
        ),
    ]
