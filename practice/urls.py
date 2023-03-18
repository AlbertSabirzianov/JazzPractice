from django.urls import path

from .views import PracticeView, PracticeResult, SucsessView, AllPracticeView

app_name = 'practice'


urlpatterns = [
    path('', PracticeView.as_view(), name='practice'),
    path('sucsess/<pk>/', SucsessView.as_view(), name='sucsess'),
    path('result/', PracticeResult.as_view(), name='result'),
    path('all/', AllPracticeView.as_view(), name='all'),
]
