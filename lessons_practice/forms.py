import random

from django import forms

from Diplom.settings import FORM_SELECT, ALL_CHORDS
from practice.models import ChordChoice, Chord, Decision


class LessonsPracticeMinorForm(forms.ModelForm):
    """Форма практики минорных аккордов."""

    CHOICES = ALL_CHORDS['minor']
    decision = forms.ChoiceField(choices=CHOICES, help_text='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.right = random.randint(Decision.MINOR, Decision.MINOR_ELEVEN)
        self.media_chord = random.choice(
            Chord.objects.filter(chord=self.right)
        )
        self.fields['decision'].widget.attrs.update(FORM_SELECT)

    class Meta:
        model = ChordChoice
        fields = ['decision', 'right_decision']


class LessonsPracticeSeptForm(forms.ModelForm):
    """Форма практики септ аккордов."""

    CHOICES = ALL_CHORDS['sept']
    decision = forms.ChoiceField(choices=CHOICES, help_text='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.right = random.randint(
            Decision.SEPT,
            Decision.SEPT_FLAT_NINE_FLAT_THIRTEEN
        )
        self.media_chord = random.choice(
            Chord.objects.filter(chord=self.right)
        )
        self.fields['decision'].widget.attrs.update(FORM_SELECT)

    class Meta:
        model = ChordChoice
        fields = ['decision', 'right_decision']


class LessonsPracticeSusForm(forms.ModelForm):
    """Форма практики sus аккордов."""

    CHOICES = ALL_CHORDS['sus']
    decision = forms.ChoiceField(choices=CHOICES, help_text='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.right = random.randint(Decision.SUS, Decision.SUS_THIRTEEN)
        self.media_chord = random.choice(
            Chord.objects.filter(chord=self.right)
        )
        self.fields['decision'].widget.attrs.update(FORM_SELECT)

    class Meta:
        model = ChordChoice
        fields = ['decision', 'right_decision']


class LessonsPracticeMajForm(forms.ModelForm):
    """Форма практики больших мажорных аккордов."""

    CHOICES = ALL_CHORDS['maj']
    decision = forms.ChoiceField(choices=CHOICES, help_text='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.right = random.randint(
            Decision.MAJ_SIX_NINE,
            Decision.MAJ_SHARP_ELEVEN
        )
        self.media_chord = random.choice(
            Chord.objects.filter(chord=self.right)
        )
        self.fields['decision'].widget.attrs.update(FORM_SELECT)

    class Meta:
        model = ChordChoice
        fields = ['decision', 'right_decision']


class LessonsPracticeMinMajForm(forms.ModelForm):
    """Форма практики минорных аккордов."""

    CHOICES = ALL_CHORDS['minor']
    decision = forms.ChoiceField(choices=CHOICES, help_text='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.right = random.randint(
            Decision.MINOR_SIX_NINE,
            Decision.MINOR_MAJ_SEVEN_NINE
        )
        self.media_chord = random.choice(
            Chord.objects.filter(chord=self.right)
        )
        self.fields['decision'].widget.attrs.update(FORM_SELECT)

    class Meta:
        model = ChordChoice
        fields = ['decision', 'right_decision']
