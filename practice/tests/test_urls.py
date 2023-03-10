from http import HTTPStatus

from django.test import TestCase, Client

from persons.models import StudentMap, User
from ..models import ChordChoice


class UrlsTestCase(TestCase):
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
            desigion=1,
            right_desigion=1,
        )
        cls.templates_name_urls = {
            '/practice/': 'practice/practice.html',
            f'/practice/sucsess/{cls.chordchoice.pk}/': 'practice/sucsess.html',
            '/practice/result/': 'practice/advice.html',
        }

    def setUp(self) -> None:
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_smoke(self):
        """Smoke test."""
        for address in self.templates_name_urls.keys():
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                self.assertEqual(response.status_code,
                                 HTTPStatus.OK,
                                 msg='Страница не найдена')

    def test_template(self):
        """Проверка соответствия шаблонов."""
        for address, template in self.templates_name_urls.items():
            with self.subTest(address=address):
                response = self.authorized_client.get(address)
                self.assertTemplateUsed(response, template)

    def test_redirect_url(self):
        """Проверка редиректов."""
        for adress in self.templates_name_urls.keys():
            with self.subTest(adress=adress):
                response = self.client.get(adress, follow=True)
                self.assertRedirects(response, f'/login/?next={adress}')
