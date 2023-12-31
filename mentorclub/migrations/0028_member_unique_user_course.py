# Generated by Django 4.2.7 on 2023-11-17 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorclub', '0027_member_user'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='member',
            constraint=models.UniqueConstraint(fields=('user', 'course'), name='unique_user_course'),
        ),
    ]
