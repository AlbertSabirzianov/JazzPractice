import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from practice.models import Chord


class AllLessons(LoginRequiredMixin, TemplateView):
    """Будет отбражаться теория по всем аккордам."""
    template_name = 'lessons/all.html'


class MinorChord(LoginRequiredMixin, TemplateView):
    """Страница о минорных септакордах."""
    template_name = 'lessons/minor.html'

    def get_context_data(self, **kwargs):
        """Добавляем музыкальные примеры на страницу."""
        context = super().get_context_data()
        context['minor_7'] = random.choice(Chord.objects.filter(chord=1))
        context['minor_9'] = random.choice(Chord.objects.filter(chord=2))
        context['minor_11'] = random.choice(Chord.objects.filter(chord=3))
        return context


class SeptChord(LoginRequiredMixin, TemplateView):
    """Страница о септакордах."""
    template_name = 'lessons/sept.html'

    def get_context_data(self, **kwargs):
        """Добавляем музыкальные примеры на страницу."""
        context = super(SeptChord, self).get_context_data()
        for number in range(4, 13):
            context[f'sept_{number}'] = random.choice(Chord.objects.filter(chord=number))
        return context


class SusChord(LoginRequiredMixin, TemplateView):
    """Страница о sus-акордах."""
    template_name = 'lessons/sus.html'

    def get_context_data(self, **kwargs):
        context = super(SusChord, self).get_context_data()
        for number in range(15, 18):
            context[f'sus_{number}'] = random.choice(Chord.objects.filter(chord=number))
        return context


class HalfDim(LoginRequiredMixin, TemplateView):
    """Страница о полууменьшенных аккордах."""
    template_name = 'lessons/half_diminished.html'

    def get_context_data(self, **kwargs):
        context = super(HalfDim, self).get_context_data()
        for number in range(13, 15):
            context[f'half_{number}'] = random.choice(Chord.objects.filter(chord=number))
        return context


class Maj(LoginRequiredMixin, TemplateView):
    """Страница о маджах."""
    template_name = 'lessons/maj.html'

    def get_context_data(self, **kwargs):
        context = super(Maj, self).get_context_data()
        for number in range(18, 21):
            context[f'maj_{number}'] = random.choice(Chord.objects.filter(chord=number))
        return context


class MinorMaj(LoginRequiredMixin, TemplateView):
    """Страница о большом минорном септакорде."""
    template_name = 'lessons/minor_maj.html'

    def get_context_data(self, **kwargs):
        contex = super(MinorMaj, self).get_context_data()
        for number in range(21, 25):
            contex[f'min_{number}'] = random.choice(Chord.objects.filter(chord=number))
        return contex
