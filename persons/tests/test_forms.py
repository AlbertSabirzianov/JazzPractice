from django.test import TestCase, Client
from django.urls import reverse

from ..models import PersonalMap, StudentMap, Feetback, User


class LoginTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.data_user = {
            'username': 'albert',
            'password1': '123456789abs',
            'password2': '123456789abs',
        }

    def test_login(self):
        """
        Тестируем создание юзера и связанных с ним
        PersonalMap, StydentMap.
        """
        user_count = User.objects.filter(is_staff=False).count()
        response = self.client.post(
            reverse('persons:registration'),
            data=self.data_user,
            follow=True,
        )

        self.assertEqual(
            User.objects.filter(is_staff=False).count(),
            user_count + 1,
            "Новый пользователь не создался"
        )
        self.assertRedirects(
            response,
            reverse('persons:success'),
        )
        self.assertTrue(
            User.objects.filter(username='albert').exists(),
            'Запись не создалась'
        )

        self.assertTrue(
            PersonalMap.objects.filter(user__username='albert').exists(),
            'PersonalMap не создалась...'
        )
        self.assertTrue(
            StudentMap.objects.filter(user__username='albert').exists(),
            "Студенческая карта не создалась..."
        )

        self.assertEqual(
            PersonalMap.objects.get(user__username='albert').stady_level,
            0,
            msg='Не присвоилось значение по умолчанию'
        )
        self.assertEqual(
            PersonalMap.objects.get(user__username='albert').stady_course,
            0,
            msg='Не присвоилось значение по умолчанию'
        )

        self.assertEqual(
            StudentMap.objects.get(user__username='albert').reiting,
            0,
            msg='Не присвоилось значение по умолчанию'
        )


class FeetbackTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            username='first',
            first_name='Bob',
            last_name='Hey',
        )
        cls.data_feetback = {
            'text': 'Text',
            'stars': 5,
        }

    def setUp(self) -> None:
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_make_feetback(self):
        """Проверяем создание отзыва."""
        feetback_count = Feetback.objects.count()
        response = self.authorized_client.post(
            reverse('persons:make_feetback'),
            data=self.data_feetback,
            follow=True,
        )

        self.assertEqual(
            Feetback.objects.count(),
            feetback_count + 1,
            msg='Не создался новый отзыв'
        )
        self.assertRedirects(
            response,
            reverse('persons:mane'),
        )
        self.assertTrue(
            Feetback.objects.filter(user=self.user).exists(),
            msg='Не создался новый отзыв'
        )

    def test_edit_feetback(self):
        """Проверяем редактирование отзыва."""
        self.feetback = Feetback.objects.create(
            pk=1,
            user=self.user,
            text='Test',
            stars=3,
        )
        feetback_count = Feetback.objects.count()

        response = self.authorized_client.post(
            reverse('persons:edit_feetback', kwargs={'pk': 1}),
            data=self.data_feetback,
            follow=True,
        )

        self.assertEqual(
            Feetback.objects.count(),
            feetback_count,
            'Создался новый пост, вместо редакции старого'
        )
        self.assertTrue(
            Feetback.objects.filter(pk=1).exists(),
            'Записи не существует'
        )
        self.assertEqual(
            Feetback.objects.get(pk=1).text,
            'Text',
            'Текст не изменился'
        )
        self.assertEqual(
            Feetback.objects.get(pk=1).stars,
            5,
            'Оценка не изменилась'
        )
        self.assertRedirects(
            response,
            reverse('persons:my_feetbacks'),
        )


class PersonalMapTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            username='first',
            first_name='Bob',
            last_name='Hey',
        )
        cls.personalmap = PersonalMap.objects.create(
            user=cls.user,
        )
        cls.data_personalmap = {
            'description': 'I am very good',
            'stady_level': 5,
            'stady_course': 1,
        }

    def setUp(self) -> None:
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_edit_personalmap(self):
        """Проверяем редактирование персональных данных."""
        personalmap_count = PersonalMap.objects.count()
        response = self.authorized_client.post(
            reverse('persons:edit_profile',
                    kwargs={'pk': self.user.pk}),
            data=self.data_personalmap,
            follow=True,
        )

        self.assertEqual(
            PersonalMap.objects.count(),
            personalmap_count,
            'Создался новый PersonalMap, вместо редакции старого'
        )
        self.assertTrue(
            PersonalMap.objects.filter(pk=self.user.pk).exists(),
            'Записи не существует'
        )
        self.assertEqual(
            PersonalMap.objects.get(pk=self.user.pk).description,
            'I am very good',
            'Текст не изменился'
        )
        self.assertEqual(
            PersonalMap.objects.get(pk=self.user.pk).stady_level,
            5,
            'stady_level не изменилась'
        )
        self.assertEqual(
            PersonalMap.objects.get(pk=self.user.pk).stady_course,
            1,
            'stady_course не изменилась'
        )
        self.assertRedirects(
            response,
            reverse('persons:person'),
        )


class DeletFeetBackTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            username='first',
            first_name='Bob',
            last_name='Hey',
        )
        cls.feetback = Feetback.objects.create(
            user=cls.user,
            text='Test',
            stars=5,
        )

    def setUp(self) -> None:
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_delete_feetback(self):
        feetback_count = Feetback.objects.count()
        response = self.authorized_client.post(
            reverse('persons:delete', kwargs={'pk': self.feetback.pk}),
            follow=True,
        )

        self.assertEqual(
            Feetback.objects.count(),
            feetback_count - 1,
            msg='Отзыв не удалился...'
        )
        self.assertFalse(
            Feetback.objects.filter(user=self.user).exists(),
            msg='Отзыв не удалился...'
        )
        self.assertRedirects(
            response,
            reverse('persons:my_feetbacks'),
        )

