# Generated by Django 3.1.4 on 2020-12-11 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checksite', '0004_site_ip_adress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='ip_adress',
            new_name='ip_address',
        ),
    ]
