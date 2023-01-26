from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, DetailView

from persons.forms import Registration, LoginForm
from persons.models import AboutSite, PersonalMap, StudentMap


class MainPage(TemplateView):
    """Главная страница."""
    template_name = 'persons/mane_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all'] = len(User.objects.filter(is_staff=False))
        return context


class Best(ListView):
    """Страничка с лучшими студентами."""
    template_name = 'persons/best.html'
    model = User
    ordering = ['username']
    queryset = User.objects.filter(is_staff=False)


class LoginUser(LoginView):
    """Страница логина."""
    form_class = LoginForm
    template_name = 'registration/login.html'


def logout_user(request):
    logout(request)
    return redirect('persons:mane')


class RegisterUser(CreateView):
    """Страница регистрации, создаёт User и Studentmap."""
    form_class = Registration
    template_name = 'persons/registration.html'
    success_url = reverse_lazy('persons:success')

    def form_valid(self, form):
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
    ordering = ['page']
    paginate_by = 1


class PersonalPage(DetailView):
    template_name = 'persons/person.html'
    model = User
