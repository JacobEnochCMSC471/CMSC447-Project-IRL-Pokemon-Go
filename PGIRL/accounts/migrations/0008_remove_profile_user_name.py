# Generated by Django 4.0.4 on 2022-05-09 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_rename_user_id_profile_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_name',
        ),
    ]