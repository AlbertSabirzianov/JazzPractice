import random
from .Datamixins.Chordmixsin import ChordDataMixin


class Chord(ChordDataMixin):
    @classmethod
    def get_new_chord(cls, number):
        return random.choice(cls.data_number_chordlist[number])


