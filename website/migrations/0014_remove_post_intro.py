# Generated by Django 3.2.9 on 2021-11-25 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_post_webmention'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='intro',
        ),
    ]
