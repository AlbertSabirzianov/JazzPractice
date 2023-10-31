from django.db import models

from persons.models import StudentMap
from Diplom.settings import Decision, MusicKey


class ChordChoice(models.Model):
    """Модель угаданного аккорда."""

    user = models.ForeignKey(StudentMap, on_delete=models.CASCADE, null=True)
    choice_time = models.DateTimeField(auto_now=True)
    decision = models.PositiveSmallIntegerField(
        verbose_name='Выберите аккорд:',
        choices=Decision.choices,
        blank=False,
        null=False,
    )
    right_decision = models.PositiveSmallIntegerField(
        verbose_name='',
        choices=Decision.choices,
        blank=True,
        null=True,
    )

    def is_right(self) -> bool:
        return self.decision == self.right_decision

    class Meta:
        verbose_name = 'Угаданный аккорд'
        verbose_name_plural = 'Угаданные аккорды'
        ordering = ['-choice_time']


class Chord(models.Model):
    """Запись Аккорда."""

    music = models.FileField(upload_to='media')
    chord = models.PositiveSmallIntegerField(
        choices=Decision.choices,
    )
    music_key = models.CharField(
        max_length=5,
        choices=MusicKey.choices
    )

    class Meta:
        verbose_name = 'Аккорд'
        verbose_name_plural = 'Аккорды'
        constraints = [
            models.UniqueConstraint(
                fields=['chord', 'music_key'],
                name='Каждая запись аккорда в одной тональности один раз.'
            )
        ]


class AccordPicture(models.Model):
    """
    Нотный пример аккорда.
    """

    picture = models.ImageField(upload_to='media')
    chord = models.PositiveSmallIntegerField(
        choices=Decision.choices,
    )
    music_key = models.CharField(
        max_length=5,
        choices=MusicKey.choices
    )

    class Meta:
        verbose_name = 'Нотный пример'
        verbose_name_plural = 'Нотные примеры'
        constraints = [
            models.UniqueConstraint(
                fields=['chord', 'music_key'],
                name='Каждый нотный пример в одной тональности один раз.'
            )
        ]
