from django.test import TestCase
from ..models import PersonalMap, Feetback, User


class TestModels(TestCase):
    """Тестируем модели."""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='first')
        cls.personalmap = PersonalMap.objects.create(user=cls.user)
        cls.feetback = Feetback.objects.create(user=cls.user, text='Text', stars=5)

    def test_str(self):
        """Проверка метода __str__()"""
        str_dict = {
            self.personalmap: 'Персональная карта  ',
            self.feetback: 'Text...'
        }

        for mod, text in str_dict.items():
            with self.subTest(model=mod):
                self.assertEqual(str(mod), text)

    def test_verbose_name(self):
        """Проверка verbose_name полей."""
        pass



