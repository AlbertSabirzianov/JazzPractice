from django.urls import path

from .views import (Best, MainPage, RegisterUser, Success, LoginUser,
                    logout_user, About, PersonalPage, MakeFeedBack, UpdateFeedBack,
                    FeedBackView, MyFeetbacks, EditProfile, DeleteFeetBack)


app_name = 'persons'

urlpatterns = [
    path('', MainPage.as_view(), name='mane'),
    path('best/', Best.as_view(), name='best'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('registation/', RegisterUser.as_view(), name='registration'),
    path('sucsess/', Success.as_view(), name='success'),
    path('about/', About.as_view(), name='about'),
    path('id/', PersonalPage.as_view(), name='person'),
    path('make_feetback/', MakeFeedBack.as_view(), name='make_feetback'),
    path('edit_feetback/<pk>/', UpdateFeedBack.as_view(), name='edit_feetback'),
    path('feetback/', FeedBackView.as_view(), name='feetback'),
    path('my_feetbacks/', MyFeetbacks.as_view(), name='my_feetbacks'),
    path('edit_profile/<pk>/', EditProfile.as_view(), name='edit_profile'),
    path('delete/<pk>/', DeleteFeetBack.as_view(), name='delete'),
]
