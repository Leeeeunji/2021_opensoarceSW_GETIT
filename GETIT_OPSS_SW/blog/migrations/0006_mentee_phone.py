# Generated by Django 3.2.7 on 2021-09-09 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_mentee_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentee',
            name='phone',
            field=models.TextField(blank=True),
        ),
    ]