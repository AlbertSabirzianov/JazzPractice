import random

from django import forms
from .models import ChordChoice, Chord


class ChordChoiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.right = random.randint(1, 24)
        self.media_chord = random.choice(Chord.objects.filter(chord=self.right))
        self.fields['desigion'].widget.attrs.update(
            {
                'class': 'form-select',
            }
        )

    class Meta:
        model = ChordChoice
        fields = ['desigion', 'right_desigion']
