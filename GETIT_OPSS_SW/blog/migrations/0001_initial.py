# Generated by Django 3.2.6 on 2021-08-20 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sexMentor', models.CharField(choices=[('Male', '남자'), ('Female', '여자')], max_length=6)),
                ('ageMentor', models.IntegerField(blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('recruit_startdate', models.DateField(default=django.utils.timezone.now, null=True)),
                ('recruit_endDate', models.DateField(default=django.utils.timezone.now, null=True)),
                ('volun_startDate', models.DateField(default=django.utils.timezone.now, null=True)),
                ('volun_endDate', models.DateField(default=django.utils.timezone.now, null=True)),
                ('volun_times', models.TextField(blank=True)),
                ('volun_day', models.TextField(blank=True)),
                ('recruit_number', models.IntegerField(blank=True, default=0)),
                ('volunType', models.CharField(choices=[('Onine', '온라인'), ('Offline', '오프라인')], max_length=10)),
                ('recruit_center', models.TextField(blank=True)),
                ('center_latitude', models.FloatField(default=0.0)),
                ('center_longitude', models.FloatField(default=0.0)),
                ('volun_place', models.TextField(blank=True)),
                ('volun_for', models.TextField(blank=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='mentee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sexMentee', models.CharField(choices=[('Male', '남자'), ('Female', '여자')], max_length=6)),
                ('ageMentee', models.IntegerField(blank=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('mentoringStart_times', models.DateField(default=django.utils.timezone.now, null=True)),
                ('mentoringEnd_times', models.DateField(default=django.utils.timezone.now, null=True)),
                ('mentoringType', models.CharField(choices=[('Onine', '온라인'), ('Offline', '오프라인')], max_length=10)),
                ('partMentor', models.CharField(choices=[('Study', '학업'), ('Digital', '디지털')], max_length=10)),
                ('recruit_center', models.TextField(blank=True)),
                ('center_latitude', models.FloatField(default=0.0)),
                ('center_longitude', models.FloatField(default=0.0)),
                ('volun_place', models.TextField(blank=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
