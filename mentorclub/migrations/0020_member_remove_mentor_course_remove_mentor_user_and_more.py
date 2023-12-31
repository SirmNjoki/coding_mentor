# Generated by Django 4.2.7 on 2023-11-17 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentorclub', '0019_remove_mentee_mentor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(max_length=50)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentorclub.course')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='course',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='user',
        ),
        migrations.AlterField(
            model_name='schedule',
            name='mentor',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='Mentee',
        ),
        migrations.DeleteModel(
            name='Mentor',
        ),
    ]
