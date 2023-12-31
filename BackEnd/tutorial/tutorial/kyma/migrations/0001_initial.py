# Generated by Django 3.1.2 on 2020-12-21 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('imgurl', models.TextField(blank=True, null=True)),
                ('smallimgurl', models.TextField(blank=True, null=True)),
                ('numpages', models.IntegerField(blank=True, null=True)),
                ('publisher', models.TextField(blank=True, null=True)),
                ('avgrating', models.FloatField(blank=True, null=True)),
                ('ratecount', models.IntegerField(blank=True, null=True)),
                ('author', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
