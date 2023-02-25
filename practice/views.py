import random

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, TemplateView, UpdateView, DeleteView, DetailView

from utils import Chord

from models import ChordChoice
from forms import ChordChoiceForm


class PracticeView(LoginRequiredMixin, CreateView):
    """Страница практики."""
    template_name = 'practice/practice.html'
    form_class = ChordChoiceForm

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.media_chord: str = None
        self.new_chord: int = None

    def get_new_chord(self):
        """Придумывает и сохраняет новый аккорд new_chord"""
        self.new_chord = random.randint(1,25)
        self.media_chord = Chord.get_new_chord(self.new_chord)

    def get_success_url(self):
        return reverse('practice:sucsess', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        """Добавляем в контекст media_chord (адрес записи аккорда mp3)."""
        context = super().get_context_data()
        self.get_new_chord()
        context['media_chord'] = self.media_chord
        return context

    def form_valid(self, form):
        """
        Сохраняет в базе ChordChoice и перенаправляет на страницу успеха.
        """
        self.object = form.save()
        self.object.right_desigion = self.new_chord
        self.object.user = self.request.user.studentmap
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class SucsessView(LoginRequiredMixin, DetailView):
    """Страничка успешной практики."""
    template_name = 'practice/sucsess.html'
    model = ChordChoice


class PracticeResult(LoginRequiredMixin, ListView):
    """Страничка с результатами практики."""
    template_name = 'practice/advice.html'
    model = ChordChoice
