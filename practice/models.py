from django.db import models
from django.utils.translation import gettext_lazy as _

from persons.models import StudentMap
from .Datamixins.Chordmixsin import ChordDataMixin


class ChordChoice(models.Model, ChordDataMixin):
    user = models.ForeignKey(StudentMap, on_delete=models.CASCADE, null=True)
    choice_time = models.DateTimeField(auto_now=True)

    class Desigion(models.IntegerChoices):
        MINOR = 1, _('m7')
        MINOR_NINE = 2, _('m9')
        MINOR_ELEVEN = 3, _('m11')
        SEPT = 4, _('7')
        SEPT_NINE = 5, _('9')
        SEPT_THIRTEEN = 6, _('13')
        SEPT_SHARP_ELEVEN = 7, _('7(#11)')
        SEPT_FLAT_NINE = 8, _('7(b9)')
        SEPT_SHARP_NINE = 9, _('7(#9)')
        # SEPT_FLAT_FIVE = 10, _('7(b5)')
        SEPT_SHARP_FIVE = 10, _('7(#5)')
        SEPT_FLAT_NINE_FLAT_THIRTEEN = 11, _('7(b9,b13)')
        SEPT_SHARP_NINE_FLAT_THIRTEEN = 12, _('7(#9,b13)')
        HALFDIMINISHED = 13, _('m7(b5)')
        HALFDIMINISHED_NINE = 14, _('m9(b5)')
        SUS = 15, _('7sus4')
        SUS_NINE = 16, _('9sus4')
        SUS_THIRTEEN = 17, _('13sus4')
        MAJ = 18, _('maj7')
        MAJ_NINE = 19, _('maj9')
        MAJ_SHARP_ELEVEN = 20, _('maj7(#11)')
        MINOR_MAJ_SEVEN = 21, _('min(maj7)')
        MINOR_MAJ_SEVEN_NINE = 22, _('min9(maj7)')
        MINOR_SIX = 23, _('min6')
        MINOR_SIX_NINE = 24, _('min6/9')

    desigion = models.PositiveSmallIntegerField(
        verbose_name='Выберите аккорд:',
        choices=Desigion.choices,
        blank=False,
        null=False,
    )
    right_desigion = models.PositiveSmallIntegerField(
        verbose_name='',
        choices=Desigion.choices,
        blank=True,
        null=True,
    )

    def is_right(self) -> bool:
        return self.desigion == self.right_desigion

    def get_desigion(self) -> str:
        return self.data_number_str[self.desigion]

    def get_right_desigion(self) -> str:
        return self.data_number_str[self.right_desigion]

    def __str__(self):
        return f'{self.user.get_full_name()} - {self.is_right()}'

    class Meta:
        ordering = ['-choice_time']


class Chord(models.Model, ChordDataMixin):
    music = models.FileField(upload_to='media')
    chord = models.PositiveSmallIntegerField(
        choices=ChordChoice.Desigion.choices,
    )


