from django.test import TestCase
from ..models import PersonalMap, StudentMap, Feetback, User


class TestModels(TestCase):
    """Тестируем модели."""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            username='first',
            first_name='Bob',
            last_name='Hey',
        )
        cls.personalmap = PersonalMap.objects.create(user=cls.user)
        cls.feetback = Feetback.objects.create(user=cls.user, text='Text', stars=5)
        cls.studentmap = StudentMap.objects.create(user=cls.user)

    def test_str(self):
        """Проверка метода __str__()"""
        str_dict = {
            self.personalmap: 'Персональная карта Hey Bob',
            self.feetback: 'Text...',
            self.studentmap: 'Учебная карта Hey Bob'
        }

        for mod, text in str_dict.items():
            with self.subTest(model=mod):
                self.assertEqual(str(mod), text)

    def test_verbose_name_personalmap(self):
        """Проверка verbose_name полей PersonalMap."""
        data = {
            'description': 'О себе',
            'stady_level': 'Уровень образования',
            'stady_course': 'Курс',
        }

        for field, text in data.items():
            with self.subTest(field=field):
                self.assertEqual(
                    self.personalmap._meta.get_field(field).verbose_name, text
                )

    def test_verbose_name_feetback(self):
        """Проверка verbose_name полей FeetBack."""
        data = {
            'text': '',
            'stars': 'Оценка',
        }

        for field, text in data.items():
            with self.subTest(field=field):
                self.assertEqual(
                    self.feetback._meta.get_field(field).verbose_name, text
                )

    def test_get_full_name(self):
        """Тест функции get_full_name() у PersonalMap."""
        self.assertEqual(
            self.personalmap.get_full_name(), 'Hey Bob'
        )

    def test_get_stady_level(self):
        """Тест функции get_stady_level() у PersonalMap."""
        self.assertEqual(
            self.personalmap.get_stady_level(), 'Не выбранно'
        )

    def test_get_stady_course(self):
        """Тест функции get_stady_course() у PersonalMap."""
        self.assertEqual(
            self.personalmap.get_stady_course(), 'Не выбранно'
        )

