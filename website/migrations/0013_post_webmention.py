# Generated by Django 3.2.9 on 2021-11-25 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_alter_post_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='webMention',
            field=models.URLField(default='', verbose_name='Webmention target'),
        ),
    ]
