# Generated by Django 4.0.5 on 2022-06-26 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_commentusers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentusers',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
