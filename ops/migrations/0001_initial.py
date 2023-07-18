# Generated by Django 4.0.1 on 2023-07-18 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(max_length=500)),
                ('number_of_pages', models.IntegerField()),
                ('price', models.IntegerField(default=199)),
            ],
        ),
    ]
