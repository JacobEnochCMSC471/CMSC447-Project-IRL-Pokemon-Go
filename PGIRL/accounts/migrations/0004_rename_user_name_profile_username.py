# Generated by Django 4.0.3 on 2022-04-27 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_experience_profile_level_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_name',
            new_name='username',
        ),
    ]