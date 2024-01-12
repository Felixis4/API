# Generated by Django 5.0.1 on 2024-01-10 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=8)),
                ('director', models.CharField(max_length=30)),
                ('studio', models.CharField(max_length=20)),
            ],
        ),
    ]
