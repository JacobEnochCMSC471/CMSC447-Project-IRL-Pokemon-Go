# Generated by Django 4.0.4 on 2022-05-17 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Photo_Uploader', '0002_rename_actual_image_photo_data_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo_data',
            name='pet_name',
            field=models.CharField(blank=True, default='Brooke', max_length=25),
        ),
    ]
