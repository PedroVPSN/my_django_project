# Generated by Django 3.1 on 2020-09-03 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ufo', '0003_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='area',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
