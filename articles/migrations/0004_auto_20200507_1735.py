# Generated by Django 3.0.4 on 2020-05-07 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200507_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='image',
            new_name='article_image',
        ),
    ]
