# Generated by Django 3.2.9 on 2021-11-09 22:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_2fa', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='device',
            unique_together={('name', 'owner')},
        ),
    ]