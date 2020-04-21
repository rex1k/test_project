# Generated by Django 2.2.2 on 2020-04-20 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HumanModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='', verbose_name='avatar')),
                ('first_name', models.CharField(max_length=40)),
                ('second_name', models.CharField(max_length=40)),
                ('age', models.PositiveIntegerField(max_length=3)),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
    ]
