# Generated by Django 3.0.1 on 2020-01-16 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epic7', '0011_buff_debuff_defensepreset_tipimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='tips',
            name='image',
            field=models.ImageField(null=True, upload_to='epic/image'),
        ),
        migrations.DeleteModel(
            name='tipImage',
        ),
    ]
