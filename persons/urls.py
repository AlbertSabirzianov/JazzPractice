from django.urls import path
from .views import Best, MainPage, RegisterUser, Success, LoginUser, logout_user, About, PersonalPage

urlpatterns = [
    path('', MainPage.as_view(), name='mane'),
    path('best/', Best.as_view(), name='best'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('registation/', RegisterUser.as_view(), name='registration'),
    path('sucsess/', Success.as_view(), name='success'),
    path('about/', About.as_view(), name='about'),
    path('id/<int:pk>', PersonalPage.as_view(), name='person')
]
