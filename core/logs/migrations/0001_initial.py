# Generated by Django 4.2.5 on 2023-09-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('ip', models.CharField(max_length=15)),
                ('user_agent', models.CharField(max_length=255)),
                ('accept_language', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]