# Generated by Django 3.1.4 on 2020-12-26 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalModel',
            fields=[
                ('idAnimal', models.AutoField(primary_key=True, serialize=False)),
                ('nombreAnimal', models.CharField(max_length=254)),
            ],
        ),
    ]
