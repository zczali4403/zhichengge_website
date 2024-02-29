# Generated by Django 5.0.2 on 2024-02-21 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_userinfo_name_userinfo_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=16)),
            ],
        ),
    ]
