# Generated by Django 2.2.19 on 2022-01-05 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20220104_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
