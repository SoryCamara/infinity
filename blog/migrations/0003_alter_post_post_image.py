# Generated by Django 4.0.5 on 2022-06-08 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_post_image_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(upload_to='post/article/', verbose_name='image'),
        ),
    ]
