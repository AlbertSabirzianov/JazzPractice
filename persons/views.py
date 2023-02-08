from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, DetailView, UpdateView

from persons.forms import Registration, LoginForm
from persons.models import AboutSite, PersonalMap, StudentMap, Feetback


class MainPage(TemplateView):
    """Главная страница."""
    template_name = 'persons/mane_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        """Добавляем в контекст количество студентов."""
        context = super().get_context_data(**kwargs)
        context['all'] = User.objects.filter(is_staff=False).count()
        return context


class Best(ListView):
    """Страничка с лучшими студентами."""
    template_name = 'persons/best.html'
    model = StudentMap


class LoginUser(LoginView):
    """Страница логина."""
    form_class = LoginForm
    template_name = 'registration/login.html'


def logout_user(request):
    """Разлогинится."""
    logout(request)
    return redirect('persons:mane')


class RegisterUser(CreateView):
    """Страница регистрации, создаёт User и Studentmap."""
    form_class = Registration
    template_name = 'persons/registration.html'
    success_url = reverse_lazy('persons:success')

    def form_valid(self, form):
        """Создаём обекты PersonalMap и StudentMap, связанные с User."""
        self.object = form.save()
        PersonalMap.objects.create(user=self.object)
        StudentMap.objects.create(user=self.object)
        return HttpResponseRedirect(self.get_success_url())


class Success(TemplateView):
    """Страница успешной регистрации."""
    template_name = 'persons/success.html'


class About(ListView):
    """
    Страница "О проекте".
    """
    template_name = 'persons/about.html'
    model = AboutSite
    paginate_by = 1


class PersonalPage(TemplateView):
    """Личная страничка."""
    template_name = 'persons/person.html'


class MakeFeedBack(CreateView):
    """Страница добавления отзыва."""
    template_name = 'persons/make_feetback.html'
    model = Feetback
    fields = ['text', 'stars']
    success_url = reverse_lazy('persons:mane')

    def form_valid(self, form):
        """Добавляем в форму Автора отзыва (поле User)."""
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class UpdateFeedBack(UpdateView):
    """Страница редактирования отзыва."""
    template_name = 'persons/edit_feetback.html'
    model = Feetback
    fields = ['text', 'stars']
    success_url = reverse_lazy('persons:mane')


class FeedBackView(ListView):
    """Страница просмотра отзывов"""
    template_name = 'persons/feetback.html'
    model = Feetback
    paginate_by = 3


class MyFeetbacks(ListView):
    """Страница моих отзывов."""
    template_name = 'persons/my_feetbaks.html'
    model = Feetback
    paginate_by = 3

    def get_queryset(self):
        """Добавляем только те отзывы, которые сделал данный пользователь."""
        queryset = self.model.objects.filter(user=self.request.user)
        return queryset


class EditProfile(UpdateView):
    """Страница редактирования личной информации."""
    template_name = 'persons/edit_profile.html'
    model = PersonalMap
    fields = ['description', 'stady_level', 'stady_course']
    success_url = reverse_lazy('persons:person')

