from django.urls import path

from .views import LessonsPracticeMajView, LessonsPracticeSusView,\
    LessonsPracticeMinorView,\
    LessonsPracticeSeptView, LessonsPracticeMinMajView

app_name = 'lessons_practice'

urlpatterns = [
    path('minor/', LessonsPracticeMinorView.as_view(), name='minor'),
    path('sept/', LessonsPracticeSeptView.as_view(), name='sept'),
    path('sus/', LessonsPracticeSusView.as_view(), name='sus'),
    path('minmaj/', LessonsPracticeMinMajView.as_view(), name='minmaj'),
    path('maj/', LessonsPracticeMajView.as_view(), name='maj'),
]
