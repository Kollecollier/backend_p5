# Generated by Django 3.2.16 on 2022-10-05 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20221005_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_kccko3', upload_to='images/'),
        ),
    ]
