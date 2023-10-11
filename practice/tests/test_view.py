from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from persons.models import StudentMap
from practice.models import ChordChoice


class ViesTestCase(TestCase):
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

    def setUp(self) -> None:
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_context_sucsess(self):
        response = self.authorized_client.get(
            reverse('practice:sucsess', kwargs={'pk': self.chordchoice.pk})
        )
        ob = response.context['object']
        self.assertEqual(
            ob.desigion,
            1
        )
        self.assertEqual(
            ob.right_decision,
            2
        )
        self.assertFalse(
            ob.is_right()
        )

    def test_result_view(self):
        response = self.authorized_client.get(
            reverse('practice:result')
        )
        ob = response.context['object_list'][0]
        self.assertEqual(
            ob.decision,
            1
        )
        self.assertEqual(
            ob.right_decision,
            2
        )
        self.assertFalse(
            ob.is_right()
        )
