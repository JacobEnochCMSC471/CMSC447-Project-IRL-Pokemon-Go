# Generated by Django 4.0.4 on 2022-05-08 23:28
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Photo_Uploader', '0011_alter_photo_data_pet_name_alter_photo_data_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo_data',
            name='pet_name',
            field=models.CharField(blank=True, default='Pamela', max_length=25),
        ),
    ]
