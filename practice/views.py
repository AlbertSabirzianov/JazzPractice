from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, TemplateView

from .forms import ChordChoiceForm
from .models import ChordChoice


class PracticeView(LoginRequiredMixin, CreateView):
    """Страница практики."""
    template_name = 'practice/practice.html'
    form_class = ChordChoiceForm

    def get_success_url(self):
        return reverse('practice:sucsess', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        """
        Сохраняет в базе ChordChoice и перенаправляет на страницу успеха.
        """
        self.object = form.save(commit=False)
        self.object.user = self.request.user.studentmap
        self.object.save()
        if self.object.is_right():
            """Если аккорд угадан, добавляем рейтинг студенту."""
            self.request.user.studentmap.reiting += 5
            self.request.user.studentmap.activiti += 1
            self.request.user.studentmap.save()
        else:
            """Если аккорд не угадан, просто добавляем очко активности."""
            self.request.user.studentmap.activiti += 1
            self.request.user.studentmap.save()
        return HttpResponseRedirect(self.get_success_url())


class SucsessView(LoginRequiredMixin, DetailView):
    """Страничка успешной практики."""
    template_name = 'practice/sucsess.html'
    model = ChordChoice


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
