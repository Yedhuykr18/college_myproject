# Generated by Django 4.0.6 on 2022-09-26 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0003_admission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admission',
            name='cont_no',
        ),
        migrations.AlterField(
            model_name='admission',
            name='obt_marks',
            field=models.PositiveIntegerField(),
        ),
    ]
