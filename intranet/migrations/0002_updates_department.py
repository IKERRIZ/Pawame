# Generated by Django 2.2.7 on 2020-01-15 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='updates',
            name='department',
            field=models.PositiveSmallIntegerField(choices=[(1, 'General'), (2, 'Human Resource'), (3, 'Information_technology'), (4, 'Inventory'), (5, 'Marketing'), (6, 'Finance')], null=True),
        ),
    ]
