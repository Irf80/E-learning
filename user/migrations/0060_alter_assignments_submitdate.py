# Generated by Django 4.2.4 on 2023-09-26 07:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0059_alter_signupmodel_submittedassignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignments',
            name='submitDate',
            field=models.DateField(default=datetime.date(2023, 9, 26)),
        ),
    ]
