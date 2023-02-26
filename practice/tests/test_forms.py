from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from persons.models import StudentMap
from ..models import ChordChoice


class PracticeFormTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            username='first',
            first_name='Bob',
            last_name='Hey',
        )
        cls.studentmap = StudentMap.objects.create(user=cls.user)
        cls.data_form = {
            'desigion': 1
        }

    def setUp(self) -> None:
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_practice(self):
        count_choice = ChordChoice.objects.count()
        response = self.authorized_client.post(
            reverse('practice:practice'),
            data=self.data_form,
            follow=True,
        )

        self.assertEqual(
            ChordChoice.objects.count(),
            count_choice + 1,
            msg='ChordChoice не создался...'
        )

        self.assertTrue(
            ChordChoice.objects.filter(user=self.studentmap).exists(),
            msg='ChordChoice не создался...'
        )
        self.chordchoice = ChordChoice.objects.get(user=self.studentmap)

        self.assertRedirects(
            response,
            reverse(
                'practice:sucsess', kwargs={
                    'pk': self.chordchoice.pk
                }
            ),
        )

        if self.chordchoice.is_right():
            number = 1
        else:
            number = 0
        self.assertEqual(
            self.studentmap.reiting,
            number,
            msg='рейтинг не добавился...'
        )

