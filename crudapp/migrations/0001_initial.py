# Generated by Django 4.0.6 on 2022-12-13 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('rollno', models.IntegerField(primary_key=True, serialize=False)),
                ('subject1', models.IntegerField()),
                ('subject2', models.IntegerField()),
            ],
        ),
    ]