import os

from django.core.files.base import ContentFile

from practice.models import Chord, AccordPicture


def push_chords_to_db():
    """Загружаем записи аккордов в базу данных."""

    chords_names = os.listdir('static/Chords')
    chords_qs = []
    for chord_name in chords_names:
        print('download...' + chord_name, end='\r')
        full_name = chord_name.split('.')[0]
        _, decision, music_key = full_name.split('_')
        with open('static/Chords/' + chord_name, 'rb') as file:
            chords_qs.append(
                Chord(
                    chord=int(decision),
                    music_key=music_key,
                    music=ContentFile(file.read(), name=chord_name)
                )
            )
    Chord.objects.bulk_create(chords_qs)


def push_pictures_of_accords_to_db():
    """
    Загружаем картинки аккордов в базу данных.
    """

    chords_names = os.listdir('static/Accords')
    chords_qs = []
    for chord_name in chords_names:
        print('download...' + chord_name, end='\r')
        full_name = chord_name.split('.')[0]
        _, decision, music_key = full_name.split('_')
        with open('static/Accords/' + chord_name, 'rb') as file:
            chords_qs.append(
                AccordPicture(
                    chord=int(decision),
                    music_key=music_key,
                    picture=ContentFile(file.read(), name=chord_name)
                )
            )
    AccordPicture.objects.bulk_create(chords_qs)
