# Generated by Django 4.2.4 on 2023-09-25 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='add', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
