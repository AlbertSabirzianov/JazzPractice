import random

from django import forms
from practice.models import ChordChoice, Chord


class LessonsPracticeMinorForm(forms.ModelForm):
    CHOICES = [
        (1, 'm7'),
        (2, 'm9'),
        (3, 'm11'),
    ]

    desigion = forms.ChoiceField(choices=CHOICES, help_text='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.right = random.randint(1, 3)
        self.media_chord = random.choice(
            Chord.objects.filter(chord=self.right)
        )
        self.fields['desigion'].widget.attrs.update(
            {
                'class': 'form-select',
            }
        )

    class Meta:
        model = ChordChoice
        fields = ['desigion', 'right_desigion']


class LessonsPracticeSeptForm(forms.ModelForm):
    CHOICES = [
        (4, '7'),
        (5, '9'),
        (6, '13'),
        (7, '7(#11)'),
        (8, '7(b9)'),
        (9, '7(#9)'),
        (10, '7(#5)'),
        (11, '7(b9,b13)'),
        (12, '7(#9,b13)'),
    ]

    desigion = forms.ChoiceField(choices=CHOICES, help_text='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.right = random.randint(4, 12)
        self.media_chord = random.choice(
            Chord.objects.filter(chord=self.right)
        )
        self.fields['desigion'].widget.attrs.update(
            {
                'class': 'form-select',
            }
        )

    class Meta:
        model = ChordChoice
        fields = ['desigion', 'right_desigion']


class LessonsPracticeSusForm(forms.ModelForm):
    CHOICES = [
        (15, '7sus4'),
        (16, '9sus4'),
        (17, '13sus4'),
    ]

    desigion = forms.ChoiceField(choices=CHOICES, help_text='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.right = random.randint(15, 17)
        self.media_chord = random.choice(
            Chord.objects.filter(chord=self.right)
        )
        self.fields['desigion'].widget.attrs.update(
            {
                'class': 'form-select',
            }
        )

    class Meta:
        model = ChordChoice
        fields = ['desigion', 'right_desigion']


class LessonsPracticeMajForm(forms.ModelForm):
    CHOICES = [
        (18, 'maj7'),
        (19, 'maj9'),
        (20, 'maj7(#11)'),
    ]

    desigion = forms.ChoiceField(choices=CHOICES, help_text='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.right = random.randint(18, 20)
        self.media_chord = random.choice(
            Chord.objects.filter(chord=self.right)
        )
        self.fields['desigion'].widget.attrs.update(
            {
                'class': 'form-select',
            }
        )

    class Meta:
        model = ChordChoice
        fields = ['desigion', 'right_desigion']


class LessonsPracticeMinMajForm(forms.ModelForm):
    CHOICES = [
        (21, 'min(maj7)'),
        (22, 'min9(maj7)'),
        (23, 'min6'),
        (24, 'min6/9'),
    ]

    desigion = forms.ChoiceField(choices=CHOICES, help_text='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.right = random.randint(21, 24)
        self.media_chord = random.choice(
            Chord.objects.filter(chord=self.right)
        )
        self.fields['desigion'].widget.attrs.update(
            {
                'class': 'form-select',
            }
        )

    class Meta:
        model = ChordChoice
        fields = ['desigion', 'right_desigion']
