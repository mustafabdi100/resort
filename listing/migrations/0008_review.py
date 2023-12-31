# Generated by Django 4.2.4 on 2023-08-09 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0007_aboutuscontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('stars', models.PositiveIntegerField(default=5)),
            ],
        ),
    ]
