# Generated by Django 3.0.3 on 2020-03-13 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='avatar',
            field=models.ImageField(upload_to='article/%Y%m%d/'),
        ),
    ]
