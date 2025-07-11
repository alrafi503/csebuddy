# Generated by Django 5.2.1 on 2025-07-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0009_subject_semester'),
    ]

    operations = [
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
            name='semester',
            field=models.IntegerField(choices=[(1, 'Semester 1'), (2, 'Semester 2'), (3, 'Semester 3'), (4, 'Semester 4'), (5, 'Semester 5'), (6, 'Semester 6'), (7, 'Semester 7')]),
        ),
        migrations.AlterField(
            model_name='subject',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='subjectfile',
            name='category',
            field=models.CharField(choices=[('notes', 'Chapter Notes'), ('question', 'Previous Year Questions'), ('suggestion', 'Suggestions'), ('syllabus', 'Syllabus'), ('others', 'Others')], max_length=20),
        ),
        migrations.AlterField(
            model_name='subjectfile',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
