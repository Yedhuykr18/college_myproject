# Generated by Django 4.0.6 on 2022-09-15 13:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='departments',
            name='dep_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='departments'),
            preserve_default=False,
        ),
    ]
