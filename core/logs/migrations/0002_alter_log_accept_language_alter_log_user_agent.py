# Generated by Django 4.2.5 on 2023-09-29 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='accept_language',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='user_agent',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
