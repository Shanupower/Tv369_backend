# Generated by Django 3.2.10 on 2023-07-07 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='cover_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]