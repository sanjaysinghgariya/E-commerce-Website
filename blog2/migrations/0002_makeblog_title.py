# Generated by Django 4.1.7 on 2023-05-02 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='makeblog',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]