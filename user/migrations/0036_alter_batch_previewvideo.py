# Generated by Django 4.2.4 on 2023-09-24 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0035_alter_batch_previewvideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='previewVideo',
            field=models.URLField(default='uou.con'),
        ),
    ]