# Generated by Django 2.2.3 on 2019-07-06 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLPair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_url', models.CharField(max_length=512)),
                ('new_url', models.CharField(max_length=128)),
            ],
        ),
    ]
