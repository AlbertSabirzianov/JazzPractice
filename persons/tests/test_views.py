from http import HTTPStatus

from django.test import TestCase, Client
from django.urls import reverse

from ..models import PersonalMap, StudentMap, Feetback, User


class ViesTestCase(TestCase):
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

    def setUp(self) -> None:
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_main_page(self):
        """Тест контекста главной страницы."""
        responce = self.client.get(reverse('persons:mane'))
        ob = responce.context['all']
        self.assertEqual(ob, 1)

    def test_best(self):
        """Тест контекста Best."""
        response = self.client.get(reverse('persons:best'))
        ob = response.context['object_list'][0]
        self.assertEqual(ob.user, self.user)

    def test_feetback(self):
        response = self.client.get(reverse('persons:feetback'))
        ob = response.context['object_list'][0]
        self.assertEqual(ob.user, self.user)
        self.assertEqual(ob.text, 'Text')
        self.assertEqual(ob.stars, 5)

    def test_my_feetback(self):
        response = self.authorized_client.get(reverse('persons:edit_feetback',
                                                      kwargs={'pk': self.feetback.pk})
                                              )
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_out_login(self):
        """Проверяем разлогин."""
        response = self.authorized_client.get(
            reverse('persons:logout'),
            follow=True,
        )

        self.assertRedirects(
            response,
            reverse('persons:mane')
        )
