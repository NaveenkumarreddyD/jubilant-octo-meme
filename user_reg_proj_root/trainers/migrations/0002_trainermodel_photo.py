# Generated by Django 2.2.5 on 2019-10-04 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainermodel',
            name='photo',
            field=models.ImageField(default='blah', upload_to='photos/%Y/%m/%d/'),
        ),
    ]
