# Generated by Django 4.0.3 on 2022-05-07 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_experience_alter_profile_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='user_id',
        ),
    ]
