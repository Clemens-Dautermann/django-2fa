# Generated by Django 3.2.10 on 2021-12-24 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_2fa', '0005_mfarequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='mfarequest',
            name='used',
            field=models.BooleanField(default=False),
        ),
    ]
