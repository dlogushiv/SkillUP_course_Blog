# Generated by Django 3.1.7 on 2021-03-11 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, max_length=120, null=True, upload_to='posts/'),
        ),
    ]
