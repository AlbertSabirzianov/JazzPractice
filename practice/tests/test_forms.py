import shutil
import tempfile

from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client, override_settings
from django.urls import reverse

from persons.models import StudentMap
from ..models import ChordChoice, Chord

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class PracticeFormTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            username='first',
            first_name='Bob',
            last_name='Hey',
        )
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x02\x00'
            b'\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xFF\xFF\xFF\x21\xF9\x04\x00\x00'
            b'\x00\x00\x00\x2C\x00\x00\x00\x00'
            b'\x02\x00\x01\x00\x00\x02\x02\x0C'
            b'\x0A\x00\x3B'
        )
        uploaded = SimpleUploadedFile(
            name='small.gif',
            content=small_gif,
            content_type='image/gif'
        )
        for i in range(1, 25):
            Chord.objects.create(chord=i, music=uploaded)
        cls.studentmap = StudentMap.objects.create(user=cls.user)
        cls.data_form = {
            'decision': 1,
            'right_decision': 1,
        }

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)

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
        self.assertTrue(
            self.chordchoice.is_right(),
            msg='xm',
        )
