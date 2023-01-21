from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from persons.forms import Registration


class MainPage(ListView):
    template_name = 'persons/mane_page.html'
    model = User

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all'] = len(User.objects.all())
        return context


class Best(ListView):
    template_name = 'persons/best.html'
    model = User
    ordering = ['username']


def into(request):
    return render(request, 'persons/into.html')


class RegisterUser(CreateView):
    form_class = Registration
    template_name = 'persons/registration.html'
    success_url = reverse_lazy('persons:success')


class Success(TemplateView):
    template_name = 'persons/success.html'
