from django.urls import path
from .views import into, Best, MainPage, RegisterUser, Success

urlpatterns = [
    path('', MainPage.as_view(), name='mane'),
    path('best/', Best.as_view(), name='best'),
    path('into/', into, name='into'),
    path('registation/', RegisterUser.as_view(), name='registration'),
    path('sucsess/', Success.as_view(), name='success')
]
