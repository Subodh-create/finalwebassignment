# Generated by Django 3.1 on 2020-08-25 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_appointment_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Picture your message'),
        ),
    ]
