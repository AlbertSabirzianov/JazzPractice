from django.contrib.auth.models import User
from django.test import TestCase

from persons.models import StudentMap
from ..models import ChordChoice


class ModelsTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            username='first',
            first_name='Bob',
            last_name='Hey',
        )
        cls.studentmap = StudentMap.objects.create(user=cls.user)
        cls.chordchoice = ChordChoice.objects.create(
            user=cls.studentmap,
            decision=1,
            right_decision=2,
        )

    def test_verbose(self):
        """Проверка verbose_name полей ChordChoice."""
        data = {
            'decision': 'Выберите аккорд:',
        }

        for field, text in data.items():
            with self.subTest(field=field):
                self.assertEqual(
                    self.chordchoice._meta.get_field(field).verbose_name, text
                )

    def test_str(self):
        """Проверка метода __str__()"""
        self.assertEqual(
            str(self.chordchoice),
            'Hey Bob'
        )

    def test_is_right(self):
        """Проверка метода is_right"""
        self.assertFalse(
            self.chordchoice.is_right(),
            msg='не работает метод is_right'
        )
