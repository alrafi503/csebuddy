from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('semester/<int:semester_num>/', views.semester_view, name='semester_view'),
    path('subject/<slug:slug>/', views.subject_detail, name='subject_detail'),
    path('syllabus/', views.syllabus_page, name='syllabus'),
    path('grade-distribution/', views.static_page, {'template_name': 'grade-distribution'}, name='grade_distribution'),
    path('notice/', views.notice_page, name='notice'),
    path('request/', views.request_docs_view, name='request_docs'),

]




