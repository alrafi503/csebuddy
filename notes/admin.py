from django.contrib import admin
from .models import Subject, SubjectFile , Notice, Syllabus

# Inline model to allow file upload within the Subject admin page
class SubjectFileInline(admin.TabularInline):
    model = SubjectFile
    extra = 1  # How many empty file fields to show by default
    fields = ('title', 'category', 'file')
    verbose_name = "Attached File"
    verbose_name_plural = "Attached Files"

# Custom admin for Subject
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'semester', 'credit', 'code')  # Display these columns in the list view
    search_fields = ('title', 'code')  # Search bar for title and code
    list_filter = ('semester',)  # Filter sidebar by semester
    inlines = [SubjectFileInline]  # Inline file editor

# Register models with admin site
admin.site.register(Subject, SubjectAdmin)
admin.site.register(SubjectFile)  # Optional: only if you want to manage files separately 

admin.site.register(Notice)
admin.site.register(Syllabus)


