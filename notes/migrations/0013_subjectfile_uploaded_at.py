# Generated by Django 5.2.1 on 2025-07-10 08:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0012_alter_subjectfile_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectfile',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
