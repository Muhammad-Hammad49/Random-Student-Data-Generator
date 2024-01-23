# Generated by Django 5.0 on 2024-01-03 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=50)),
                ('movie_desc', models.CharField(max_length=200)),
                ('movie_img', models.ImageField(upload_to='')),
            ],
        ),
    ]