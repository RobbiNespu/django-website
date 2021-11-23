# Generated by Django 3.2.9 on 2021-11-21 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_post_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'get_latest_by': 'creation_date', 'ordering': ['-creation_date']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='date_added',
            new_name='creation_date',
        ),
        migrations.AddField(
            model_name='post',
            name='modification_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-creation_date'], name='website_pos_creatio_b77311_idx'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='website.Tag'),
        ),
    ]