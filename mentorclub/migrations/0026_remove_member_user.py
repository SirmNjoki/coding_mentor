# Generated by Django 4.2.7 on 2023-11-17 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentorclub', '0025_alter_member_experience_alter_member_interest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='user',
        ),
    ]
