# Generated by Django 2.2.5 on 2019-10-01 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('batchapp', '0003_auto_20190930_0808'),
        ('courseapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('select_batch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='batchapp.Batch')),
                ('select_course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courseapp.CourseModel')),
            ],
        ),
    ]
