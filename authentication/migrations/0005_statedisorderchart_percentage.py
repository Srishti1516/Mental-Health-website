# Generated by Django 3.1.1 on 2020-09-29 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_statedisorderchart'),
    ]

    operations = [
        migrations.AddField(
            model_name='statedisorderchart',
            name='percentage',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
