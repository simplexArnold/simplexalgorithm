# Generated by Django 3.1.1 on 2021-02-07 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No', models.IntegerField()),
                ('Name', models.CharField(max_length=25)),
                ('Age', models.IntegerField()),
                ('Mob', models.IntegerField()),
                ('Add', models.CharField(max_length=64)),
            ],
        ),
    ]
