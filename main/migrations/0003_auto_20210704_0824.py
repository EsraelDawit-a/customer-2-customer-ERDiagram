# Generated by Django 3.2.5 on 2021-07-04 08:24

from django.db import migrations, models
import main.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210704_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagorie',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='subcatagorie',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='subcatagorie',
            name='field',
            field=main.db_fields.ListField(token=','),
        ),
    ]
