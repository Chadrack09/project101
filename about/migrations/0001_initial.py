# Generated by Django 2.2 on 2019-07-27 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('catchy', models.CharField(max_length=400)),
                ('body', models.TextField()),
            ],
        ),
    ]
