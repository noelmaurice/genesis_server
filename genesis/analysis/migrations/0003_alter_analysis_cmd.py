# Generated by Django 3.2.5 on 2021-07-26 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0002_auto_20210726_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='cmd',
            field=models.TextField(null=True),
        ),
    ]