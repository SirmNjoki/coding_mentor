# Generated by Django 4.2.7 on 2023-11-16 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentorclub', '0016_course_date_course_description_course_fromt_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='fromT',
        ),
        migrations.RemoveField(
            model_name='course',
            name='toT',
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=15000)),
                ('date', models.DateField()),
                ('fromT', models.TimeField()),
                ('toT', models.TimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentorclub.course')),
            ],
        ),
    ]
