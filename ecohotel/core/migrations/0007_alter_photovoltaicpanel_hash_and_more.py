# Generated by Django 4.0.5 on 2022-10-24 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_greenenergy_photovoltaicpanel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photovoltaicpanel',
            name='hash',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='photovoltaicpanel',
            name='txId',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
    ]