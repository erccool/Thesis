# Generated by Django 2.0.4 on 2018-04-05 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SOM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_name', models.CharField(max_length=250)),
                ('path', models.CharField(max_length=500)),
            ],
        ),
    ]
