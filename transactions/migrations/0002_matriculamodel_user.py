# Generated by Django 5.1.7 on 2025-03-28 03:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matriculamodel',
            name='user',
            field=models.ForeignKey(blank=True, db_column='user', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matricula', to='authentication.usermodel'),
        ),
    ]
