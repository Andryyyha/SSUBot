# Generated by Django 2.2.4 on 2019-08-07 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('df_handler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayOfWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='building',
            name='building_number',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_number',
            field=models.CharField(max_length=6),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_handler.ClassName')),
            ],
        ),
    ]
