# Generated by Django 5.2.1 on 2025-07-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_remove_subject_description_remove_subject_file_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='course_code',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='credit',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='slug',
        ),
        migrations.AddField(
            model_name='subject',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='subject_files/'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='image',
            field=models.ImageField(upload_to='subject_images/'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='semester',
            field=models.CharField(choices=[('1', 'Semester 1'), ('2', 'Semester 2'), ('3', 'Semester 3'), ('4', 'Semester 4'), ('5', 'Semester 5'), ('6', 'Semester 6'), ('7', 'Semester 7'), ('8', 'Semester 8')], max_length=1),
        ),
        migrations.AlterField(
            model_name='subject',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
