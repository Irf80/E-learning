# Generated by Django 4.2.4 on 2023-09-19 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_signupmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupmodel',
            name='image',
            field=models.ImageField(upload_to='user/images'),
        ),
    ]
