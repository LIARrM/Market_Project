# Generated by Django 4.2.6 on 2024-08-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default=1, upload_to='avatars/'),
            preserve_default=False,
        ),
    ]
