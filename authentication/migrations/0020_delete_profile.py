# Generated by Django 3.1.2 on 2020-11-17 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0019_delete_anonymous_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]