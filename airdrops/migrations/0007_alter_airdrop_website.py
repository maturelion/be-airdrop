# Generated by Django 5.0.3 on 2024-03-20 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airdrops', '0006_alter_airdrop_ticker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airdrop',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]