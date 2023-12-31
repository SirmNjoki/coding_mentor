# Generated by Django 4.2.7 on 2023-11-18 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorclub', '0031_alter_member_course'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='schedule',
            constraint=models.UniqueConstraint(fields=('course', 'mentor'), name='unique_course_mentor'),
        ),
    ]
