# Generated by Django 3.2.7 on 2021-09-09 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210909_2007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentee',
            old_name='recruit_endDate2',
            new_name='endDate',
        ),
        migrations.RenameField(
            model_name='mentee',
            old_name='recruit_center',
            new_name='grade',
        ),
        migrations.RenameField(
            model_name='mentee',
            old_name='recruit_startdate2',
            new_name='startdate',
        ),
        migrations.RenameField(
            model_name='mentee',
            old_name='volun_day',
            new_name='study_day',
        ),
        migrations.RenameField(
            model_name='mentee',
            old_name='volun_for',
            new_name='study_place',
        ),
        migrations.RemoveField(
            model_name='mentee',
            name='volun_place',
        ),
    ]