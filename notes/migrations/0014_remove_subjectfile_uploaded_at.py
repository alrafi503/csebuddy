# Generated by Django 5.2.1 on 2025-07-10 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0013_subjectfile_uploaded_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjectfile',
            name='uploaded_at',
        ),
    ]
