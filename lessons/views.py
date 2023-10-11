from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class AllLessons(LoginRequiredMixin, TemplateView):
    """Будет отбражаться теория по всем аккордам."""

    template_name = 'lessons/all.html'


class MinorChord(LoginRequiredMixin, TemplateView):
    """Страница о минорных септакордах."""

    template_name = 'lessons/minor.html'


class SeptChord(LoginRequiredMixin, TemplateView):
    """Страница о септакордах."""

    template_name = 'lessons/sept.html'


class SusChord(LoginRequiredMixin, TemplateView):
    """Страница о sus-акордах."""

    template_name = 'lessons/sus.html'


class HalfDim(LoginRequiredMixin, TemplateView):
    """Страница о полууменьшенных аккордах."""

    template_name = 'lessons/half_diminished.html'


class Maj(LoginRequiredMixin, TemplateView):
    """Страница о больших мажорных септаккордах."""

    template_name = 'lessons/maj.html'


class MinorMaj(LoginRequiredMixin, TemplateView):
    """Страница о большом минорном септакорде."""

    template_name = 'lessons/minor_maj.html'
