# Generated by Django 4.2.4 on 2024-01-15 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_proifle_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.CharField(default='https://cdn-icons-png.flaticon.com/512/21/21294.png', max_length=255),
        ),
    ]
