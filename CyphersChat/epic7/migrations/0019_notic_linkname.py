# Generated by Django 3.0.2 on 2020-01-18 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epic7', '0018_notic_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='notic',
            name='linkName',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
