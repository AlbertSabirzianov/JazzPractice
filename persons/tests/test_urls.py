from http import HTTPStatus

from django.test import TestCase, Client

from ..models import PersonalMap, StudentMap, User, Feetback


class UrlsTestCase(TestCase):
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
        cls.templates_name_urls = {
            '': 'persons/mane_page.html',
            '/best/': 'persons/best.html',
            '/login/': 'registration/login.html',
            '/registation/': 'persons/registration.html',
            '/sucsess/': 'persons/success.html',
            '/about/': 'persons/about.html',
            '/id/': 'persons/person.html',
            '/make_feetback/': 'persons/make_feetback.html',
            f'/edit_feetback/{cls.feetback.pk}/': 'persons/edit_feetback.html',
            '/feetback/': 'persons/feetback.html',
            '/my_feetbacks/': 'persons/my_feetbaks.html',
            f'/edit_profile/{cls.personalmap.pk}/': 'persons/edit_profile.html',
            f'/delete/{cls.feetback.pk}/': 'persons/delet_feetback.html',
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

    def test_unexiting_page(self):
        """Проверка несуществующей страницы."""
        self.assertEqual(
            self.authorized_client.get('/unexiting_page/').status_code,
            HTTPStatus.NOT_FOUND
        )

    def test_redirect_url(self):
        """Проверка редиректов."""
        response = self.client.get('/id/', follow=True)
        self.assertRedirects(response, '/login/?next=/id/')

        response = self.client.get('/make_feetback/', follow=True)
        self.assertRedirects(response, '/login/?next=/make_feetback/')

        response = self.client.get(f'/edit_feetback/{self.feetback.pk}/', follow=True)
        self.assertRedirects(response, f'/login/?next=/edit_feetback/{self.feetback.pk}/')

        response = self.client.get('/my_feetbacks/', follow=True)
        self.assertRedirects(response, '/login/?next=/my_feetbacks/')

        response = self.client.get(f'/edit_profile/{self.personalmap.pk}/', follow=True)
        self.assertRedirects(response, f'/login/?next=/edit_profile/{self.personalmap.pk}/')

        response = self.client.get(f'/delete/{self.feetback.pk}/', follow=True)
        self.assertRedirects(response, f'/login/?next=/delete/{self.feetback.pk}/')

