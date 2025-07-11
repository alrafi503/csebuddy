from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator

class Subject(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=20, blank=True, null=True)
    credit = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='subject_images/', blank=True, null=True)
    semester = models.IntegerField(choices=[(i, f'Semester {i}') for i in range(1, 9)])  
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-semester-{self.semester}")
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.title} (Semester {self.semester})"
    
class Meta:
        ordering = ['semester', 'title']

class SubjectFile(models.Model):
    FILE_CATEGORIES = [
        ('notes', '📘 Chapter Notes'),
        ('question', '📄 Previous Year Questions'),
        ('suggestion', '📑 Suggestions'),
        ('syllabus', '📚 Syllabus'),
        ('Book', '🧾 Book'),
    ]
    
    subject = models.ForeignKey(Subject, related_name='files', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=FILE_CATEGORIES)
    file = models.FileField(
        upload_to='subject_files/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'ppt', 'pptx', 'zip'])]
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.subject.title} - {self.title}"
    
class Meta:
        ordering = ['category', 'title']

from django.db import models
from django.utils import timezone


class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    attachment = models.FileField(
        upload_to='notices/', 
        blank=True, 
        null=True,
        help_text="Optional: Upload an image or document (PDF, JPG, PNG)"
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Syllabus(models.Model):
    semester = models.IntegerField(choices=[(i, f'Semester {i}') for i in range(1, 9)])
    pdf_file = models.FileField(upload_to='syllabus_pdfs/')

    def __str__(self):
        return f"Semester {self.semester} Syllabus"




