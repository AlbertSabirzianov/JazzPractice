from django.urls import path

from . import views

app_name = 'lessons'

urlpatterns = [
    path('all/', views.AllLessons.as_view(), name='all'),
    path('minor/', views.MinorChord.as_view(), name='minor'),
    path('sept/', views.SeptChord.as_view(), name='sept'),
    path('sus/', views.SusChord.as_view(), name='sus'),
    path('half_diminished/', views.HalfDim.as_view(), name='half_dim'),
    path('maj/', views.Maj.as_view(), name='maj'),
    path('minor_maj/', views.MinorMaj.as_view(), name='minor_maj'),
]
