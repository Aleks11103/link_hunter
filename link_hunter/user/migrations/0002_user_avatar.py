# Generated by Django 3.1.5 on 2021-02-22 16:23

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to=user.models.User.path_upload, verbose_name='Avatar'),
        ),
    ]
