from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import TestCase, Client


class LessonsUrlsTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            username='first',
            first_name='Bob',
            last_name='Hey',
        )
        cls.templates_name_urls = {
            '/lessons/all/': 'lessons/all.html',
            '/lessons/minor/': 'lessons/minor.html',
            '/lessons/sept/': 'lessons/sept.html',
            '/lessons/sus/': 'lessons/sus.html',
            '/lessons/half_diminished/': 'lessons/half_diminished.html',
            '/lessons/maj/': 'lessons/maj.html',
            '/lessons/minor_maj/': 'lessons/minor_maj.html',
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



