# Generated by Django 5.2.1 on 2025-07-07 15:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_remove_subject_course_code_remove_subject_credit_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='file',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='semester',
        ),
        migrations.AddField(
            model_name='subject',
            name='code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='credit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subject',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='subject_images/'),
        ),
        migrations.CreateModel(
            name='SubjectFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='subject_files/')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='notes.subject')),
            ],
        ),
    ]
