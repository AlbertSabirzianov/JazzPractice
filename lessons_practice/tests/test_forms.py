import shutil
import tempfile

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client, override_settings
from django.urls import reverse

from persons.models import StudentMap, User
from practice.models import Chord, ChordChoice, AccordPicture
from Diplom.settings import MusicKey

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class UrlsTestCase(TestCase):
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
        for i in range(1, 29):
            Chord.objects.create(chord=i, music=uploaded)
            AccordPicture.objects.create(chord=i, music_key=MusicKey.G)
            AccordPicture.objects.create(chord=i, music_key=MusicKey.C)
        cls.studentmap = StudentMap.objects.create(user=cls.user)


    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)

    def setUp(self) -> None:
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_minor_form(self):
        count_choice = ChordChoice.objects.count()
        response = self.authorized_client.post(
            reverse('lessons_practice:minor'),
            data={'decision': 1, 'right_decision': 1}
        )

        self.assertEqual(
            ChordChoice.objects.count(),
            count_choice + 1,
            msg='ChordChoice не создался...'
        )

        self.assertTrue(
            ChordChoice.objects.filter(user=self.studentmap, decision=1).exists(),
            msg='ChordChoice не создался...'
        )

        chordchoice = ChordChoice.objects.get(user=self.studentmap, decision=1)

        self.assertRedirects(
            response,
            reverse(
                'practice:sucsess', kwargs={
                    'pk': chordchoice.pk
                }
            ),
        )

    def test_sept_form(self):
        count_choice = ChordChoice.objects.count()
        response = self.authorized_client.post(
            reverse('lessons_practice:sept'),
            data={'decision': 5, 'right_decision': 5}
        )

        self.assertEqual(
            ChordChoice.objects.count(),
            count_choice + 1,
            msg='ChordChoice не создался...'
        )

        self.assertTrue(
            ChordChoice.objects.filter(user=self.studentmap, decision=5).exists(),
            msg='ChordChoice не создался...'
        )

        chordchoice = ChordChoice.objects.get(user=self.studentmap, decision=5)

        self.assertRedirects(
            response,
            reverse(
                'practice:sucsess', kwargs={
                    'pk': chordchoice.pk
                }
            ),
        )

    def test_sus_form(self):
        count_choice = ChordChoice.objects.count()
        response = self.authorized_client.post(
            reverse('lessons_practice:sus'),
            data={'decision': 19, 'right_decision': 19}
        )

        self.assertEqual(
            ChordChoice.objects.count(),
            count_choice + 1,
            msg='ChordChoice не создался...'
        )

        self.assertTrue(
            ChordChoice.objects.filter(user=self.studentmap, decision=19).exists(),
            msg='ChordChoice не создался...'
        )

        chordchoice = ChordChoice.objects.get(user=self.studentmap, decision=19)

        self.assertRedirects(
            response,
            reverse(
                'practice:sucsess', kwargs={
                    'pk': chordchoice.pk
                }
            ),
        )

    def test_minmaj_form(self):
        count_choice = ChordChoice.objects.count()
        response = self.authorized_client.post(
            reverse('lessons_practice:minmaj'),
            data={'decision': 26, 'right_decision': 26}
        )

        self.assertEqual(
            ChordChoice.objects.count(),
            count_choice + 1,
            msg='ChordChoice не создался...'
        )

        self.assertTrue(
            ChordChoice.objects.filter(user=self.studentmap, decision=26).exists(),
            msg='ChordChoice не создался...'
        )

        chordchoice = ChordChoice.objects.get(user=self.studentmap, decision=26)

        self.assertRedirects(
            response,
            reverse(
                'practice:sucsess', kwargs={
                    'pk': chordchoice.pk
                }
            ),
        )

    def test_maj_form(self):
        count_choice = ChordChoice.objects.count()
        response = self.authorized_client.post(
            reverse('lessons_practice:maj'),
            data={'decision': 22, 'right_decision': 22}
        )

        self.assertEqual(
            ChordChoice.objects.count(),
            count_choice + 1,
            msg='ChordChoice не создался...'
        )

        self.assertTrue(
            ChordChoice.objects.filter(user=self.studentmap, decision=22).exists(),
            msg='ChordChoice не создался...'
        )

        chordchoice = ChordChoice.objects.get(user=self.studentmap, decision=22)

        self.assertRedirects(
            response,
            reverse(
                'practice:sucsess', kwargs={
                    'pk': chordchoice.pk
                }
            ),
        )
