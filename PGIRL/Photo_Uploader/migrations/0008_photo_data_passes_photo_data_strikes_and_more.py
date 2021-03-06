# Generated by Django 4.0.3 on 2022-04-26 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Photo_Uploader', '0007_alter_photo_data_pet_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo_data',
            name='passes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='photo_data',
            name='strikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='photo_data',
            name='pet_name',
            field=models.CharField(blank=True, default='Trevor', max_length=25),
        ),
    ]
