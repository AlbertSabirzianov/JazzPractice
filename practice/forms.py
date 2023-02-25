from django import forms
from .models import ChordChoice


class ChordChoiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['desigion'].widget.attrs.update(
            {
                'class': 'form-select',
            }
        )

    class Meta:
        model = ChordChoice
        fields = ['desigion']
