from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class StudentMap(models.Model):
    """Модель с данными студента, связана с аккаунтом  User."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    reiting = models.PositiveSmallIntegerField(_('Рейтинг'), default=0)
    start_study = models.DateTimeField(_('Начало обучения'), auto_now=True)
    graduate = models.BooleanField(_('Закончил курс'), default=False)

    def __str__(self):
        return f'Учебная карта {self.user.username}'


class PersonalMap(models.Model):
    """Модель с личными данными студента."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField(_('О себе'), null=True, blank=True)

    class Institutions(models.IntegerChoices):
        """
        Выбор уровня образования.
        """
        NOCHOICE = 0, _('Не выбранно')
        NO = 1, _('Нет музыкального образования')
        SCHOOL = 2, _('Музыкальная школа')
        COLLEGE = 3, _('Среднее музыкальное образование')
        YNIVER = 4, _('Бакалавриат')
        MAG = 5, _('Магистратура')
        ASS = 6, _('Аспирантура')

    stady_level = models.PositiveSmallIntegerField(_('Уровень образования'),
                                                   choices=Institutions.choices,
                                                   default=0)

    def __str__(self):
        return f'Персональная карта {self.user.username}'

    class Course(models.IntegerChoices):
        """
        Выбор курса.
        """
        NOT = 0, _('Нет музыкального образования')
        ONE = 1, _('1й')
        THO = 2, _('2й')
        THREE = 3, _('3й')
        FOUR = 4, _('4й')
        FIVE = 5, _('5й')

    stady_course = models.PositiveSmallIntegerField(_('Курс'), choices=Course.choices, default=0)


class AboutSite(models.Model):
    text = models.TextField(_('О сайте'), null=False, blank=False)
    page = models.PositiveSmallIntegerField(_('Страничка'))

    def __str__(self):
        return f'О сайте страница - {self.page}'
