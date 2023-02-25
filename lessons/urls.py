from django.urls import path
from .views import AllLessons, MinorChord, SeptChord, SusChord, HalfDim, Maj, MinorMaj

app_name = 'lessons'

urlpatterns = [
    path('all/', AllLessons.as_view(), name='all'),
    path('minor/', MinorChord.as_view(), name='minor'),
    path('sept/', SeptChord.as_view(), name='sept'),
    path('sus/', SusChord.as_view(), name='sus'),
    path('half_diminished/', HalfDim.as_view(), name='half_dim'),
    path('maj/', Maj.as_view(), name='maj'),
    path('minor_maj/', MinorMaj.as_view(), name='minor_maj'),
]

