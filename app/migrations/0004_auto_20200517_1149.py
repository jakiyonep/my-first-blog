# Generated by Django 3.0.5 on 2020-05-17 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_contentimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentimage',
            name='content_image',
            field=models.ImageField(upload_to='post_content_images/'),
        ),
    ]
