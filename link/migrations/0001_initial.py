# Generated by Django 4.0.5 on 2022-06-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro', models.CharField(default='Infinity Media', max_length=255, verbose_name='Text')),
                ('fb_link', models.URLField()),
                ('twitter_link', models.URLField()),
                ('instagram_link', models.URLField()),
            ],
        ),
    ]