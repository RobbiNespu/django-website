# Generated by Django 3.2.9 on 2021-12-13 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_auto_20211213_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.indiewebsource'),
        ),
    ]
