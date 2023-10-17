from django.core.management import BaseCommand

from art import text2art

from core.services import push_chords_to_db, push_pictures_of_accords_to_db


class Command(BaseCommand):
    """
    Загружаем аккорды в базу данных.
    """

    def handle(self, *args, **options):
        print(text2art('start'))
        push_chords_to_db()
        push_pictures_of_accords_to_db()
        print(text2art('susses'))
