# Generated by Django 5.1.6 on 2025-03-05 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reset_token',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
