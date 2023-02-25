from django.urls import path

from .views import PracticeView, PracticeResult, SucsessView

app_name = 'practice'


urlpatterns = [
    path('', PracticeView.as_view(), name='practice'),
    path('sucsess/<pk>/', SucsessView.as_view(), name='sucsess'),
    path('result/', PracticeResult.as_view(), name='result'),
]
