# Generated by Django 4.2.4 on 2023-08-08 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='num_beds',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='room',
            name='num_people',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='room_images/')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='listing.room')),
            ],
        ),
    ]
