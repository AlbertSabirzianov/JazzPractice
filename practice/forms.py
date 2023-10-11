import random

from django import forms

from .models import ChordChoice, Chord, Decision
from Diplom.settings import FORM_SELECT


class ChordChoiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.right = random.randint(Decision.MINOR, Decision.MINOR_MAJ_SEVEN_NINE)
        self.media_chord = random.choice(Chord.objects.filter(chord=self.right))
        self.fields['decision'].widget.attrs.update(FORM_SELECT)

    class Meta:
        model = ChordChoice
        fields = ['decision', 'right_decision']
