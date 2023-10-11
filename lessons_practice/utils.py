from typing import Type

from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView
from django.db.models import F

from .forms import LessonsPracticeMajForm, LessonsPracticeSeptForm,\
    LessonsPracticeSusForm, LessonsPracticeMinorForm, \
    LessonsPracticeMinMajForm
from practice.forms import ChordChoiceForm


FORMS_DICT: dict[str, Type[forms.ModelForm]] = {
    'all': ChordChoiceForm,
    'minor': LessonsPracticeMinorForm,
    'sus': LessonsPracticeSusForm,
    'maj': LessonsPracticeMajForm,
    'sept': LessonsPracticeSeptForm,
    'minmaj': LessonsPracticeMinMajForm,
}

REITING_DICT: dict[str, int] = {
    'all': 5,
    'minor': 1,
    'sus': 1,
    'maj': 1,
    'sept': 3,
    'minmaj': 2,
}


class LessonsPracticeView(LoginRequiredMixin, CreateView):
    template_name = 'practice/practice.html'
    lesson_type = ''

    def get_form_class(self):
        return FORMS_DICT[self.lesson_type]

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
            """Если аккорд угадан, добавляем рейтинг студенту и активность."""
            self.request.user.studentmap.reiting = F('reiting') + REITING_DICT[
                self.lesson_type
            ]
            self.request.user.studentmap.activiti = F('activiti') + 1
            self.request.user.studentmap.save()
        else:
            """Если аккорд не угадан, просто добавляем очко активности."""
            self.request.user.studentmap.activiti = F('activiti') + 1
            self.request.user.studentmap.save()
        return HttpResponseRedirect(self.get_success_url())
