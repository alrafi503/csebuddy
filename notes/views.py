from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from .models import Subject, SubjectFile
from django.db.models import Q

def home(request):
    query = request.GET.get('q')
    if query:
        subjects = Subject.objects.filter(
            Q(title__icontains=query) |
            Q(code__icontains=query) |
            Q(description__icontains=query)
        ).distinct().order_by('semester', 'title')
        return render(request, 'index.html', {
            'subjects': subjects,
            'query': query,
            'search_performed': True,
        })
    return render(request, 'index.html')

def get_category_icon(category_type):
    icons = {
        'notes': 'bi-journal-text',
        'question': 'bi-question-circle',
        'suggestion': 'bi-lightbulb',
        'syllabus': 'bi-file-earmark-text',
        'Book': 'bi-file-earmark'
    }
    return icons.get(category_type, 'bi-file-earmark')

def semester_view(request, semester_num):
    if not 1 <= semester_num <= 8:
        raise Http404("Semester does not exist (choose 1-8)")
    
    subjects = Subject.objects.filter(semester=semester_num).order_by('code').prefetch_related('files')
    paginator = Paginator(subjects, 10)  # 10 subjects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Organize files by category for display
    for subject in page_obj:
        subject.resource_categories = []
        for category in SubjectFile.FILE_CATEGORIES:
            files = subject.files.filter(category=category[0])
            if files.exists():
                subject.resource_categories.append({
                    'name': category[1],
                    'count': files.count(),
                    'icon': get_category_icon(category[0])  # Note: removed self.
                })
    
    return render(request, 'semester.html', {
        'subjects': page_obj,
        'semester_num': semester_num,
        'file_categories': SubjectFile.FILE_CATEGORIES,
    })

def subject_detail(request, slug):
    """
    Detailed view for a subject with organized files by category
    using prefetch_related for better performance
    """
    subject = get_object_or_404(
        Subject.objects.prefetch_related('files'),
        slug=slug
    )
    
    # Organize files by category with count
    file_categories = {
        category[1]: subject.files.filter(category=category[0])
        for category in SubjectFile.FILE_CATEGORIES
        if subject.files.filter(category=category[0]).exists()
    }
    
    return render(request, 'subject_detail.html', {
        'subject': subject,
        'file_categories': file_categories,
    })

def static_page(request, template_name):
    """
    Generic view for static pages with 404 handling
    """
    valid_pages = ['syllabus', 'grade-distribution', 'notice', 'request']
    if template_name not in valid_pages:
        raise Http404("Page not found")
    
    return render(request, f'dropdown/{template_name}.html')

from django.db.models import Q

def search_results(request):
    # This is a backup view if you want a separate search results page
    query = request.GET.get('q')
    subjects = Subject.objects.filter (
        Q(title__icontains=query) |
        Q(code__icontains=query) )
    return render(request, 'index.html', {
        'subjects': subjects,
        'query': query
    }) 

from .models import Notice, Syllabus

def notice_page(request):
    notices = Notice.objects.all().order_by('-created_at')
    return render(request, 'dropdown/notice.html', {'notices': notices})

def syllabus_page(request):
    syllabi = Syllabus.objects.all()
    syllabus_links = {entry.semester: entry.pdf_file.url for entry in syllabi}
    return render(request, 'dropdown/syllabus.html', {'syllabus_links': syllabus_links})

from .models import Subject

def request_docs_view(request):
    subjects = Subject.objects.all().order_by('semester', 'title')
    return render(request, 'dropdown/request.html', {'subjects': subjects})
