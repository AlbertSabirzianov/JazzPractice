from django.urls import path

from . import views


app_name = 'persons'

urlpatterns = [
    path('', views.MainPage.as_view(), name='mane'),
    path('best/', views.Best.as_view(), name='best'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('registation/', views.RegisterUser.as_view(), name='registration'),
    path('sucsess/', views.Success.as_view(), name='success'),
    path('about/', views.About.as_view(), name='about'),
    path('id/', views.PersonalPage.as_view(), name='person'),
    path('make_feetback/', views.MakeFeedBack.as_view(), name='make_feetback'),
    path('edit_feetback/<pk>/', views.UpdateFeedBack.as_view(), name='edit_feetback'),
    path('feetback/', views.FeedBackView.as_view(), name='feetback'),
    path('my_feetbacks/', views.MyFeetbacks.as_view(), name='my_feetbacks'),
    path('edit_profile/<pk>/', views.EditProfile.as_view(), name='edit_profile'),
    path('delete/<pk>/', views.DeleteFeetBack.as_view(), name='delete'),
]
