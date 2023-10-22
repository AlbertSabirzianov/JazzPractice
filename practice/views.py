from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView

from Diplom.settings import MusicKey
from lessons_practice.utils import LessonsPracticeView
from .models import ChordChoice, AccordPicture, Chord


class PracticeView(LessonsPracticeView):
    """Страница практики по всем аккордам."""

    lesson_type = 'all'


class SucsessView(LoginRequiredMixin, DetailView):
    """Страничка успешной практики."""

    template_name = 'practice/sucsess.html'
    model = ChordChoice

    def get_context_data(self, **kwargs):
        """Добавляем нотные примеры на страницу успеха."""

        context = super().get_context_data()
        context['accord_C'] = AccordPicture.objects.get(
            chord=self.object.right_decision,
            music_key=MusicKey.C
        )
        context['accord_G'] = AccordPicture.objects.get(
            chord=self.object.right_decision,
            music_key=MusicKey.G
        )
        context['chord_C'] = Chord.objects.get(
            chord=self.object.right_decision,
            music_key=MusicKey.C
        )
        context['chord_G'] = Chord.objects.get(
            chord=self.object.right_decision,
            music_key=MusicKey.G
        )
        return context


class PracticeResult(LoginRequiredMixin, ListView):
    """Страничка с результатами практики."""

    template_name = 'practice/advice.html'
    model = ChordChoice

    def get_queryset(self):
        """Выбираем только те результаты, которые принадлежат студенту."""

        queryset = self.model.objects.filter(
            user=self.request.user.studentmap
        )[:20]
        return queryset


class AllPracticeView(TemplateView):
    """Страничка всех видов практики."""

    template_name = 'practice/all.html'
