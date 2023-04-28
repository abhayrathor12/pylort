# Generated by Django 4.2 on 2023-04-24 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('fees', models.IntegerField(default=50)),
                ('phone', models.IntegerField()),
                ('joined_date', models.DateField()),
                ('cour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stu_app.courses')),
                ('dur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stu_app.duration')),
            ],
        ),
    ]
