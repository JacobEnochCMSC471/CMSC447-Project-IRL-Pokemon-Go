# Generated by Django 4.0.3 on 2022-05-06 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Photo_Uploader', '0008_photo_data_passes_photo_data_strikes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo_data',
            name='pet_name',
            field=models.CharField(blank=True, default='Johnny', max_length=25),
        ),
        migrations.AlterField(
            model_name='photo_data',
            name='user_id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
