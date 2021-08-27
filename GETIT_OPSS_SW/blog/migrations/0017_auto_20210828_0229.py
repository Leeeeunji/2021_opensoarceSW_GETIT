# Generated by Django 3.2.6 on 2021-08-27 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_mentee_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentee',
            old_name='partMentor',
            new_name='mentoringPart',
        ),
        migrations.AlterField(
            model_name='mentee',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
