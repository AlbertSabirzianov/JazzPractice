import shutil
import tempfile
from http import HTTPStatus

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client, override_settings

from Diplom.settings import MusicKey
from persons.models import StudentMap, User
from practice.models import Chord, ChordChoice, AccordPicture

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
        cls.chordchoice = ChordChoice.objects.create(
            user=cls.studentmap,
            decision=1,
            right_decision=1,
        )
        cls.templates_name_urls = {
            '/lessons_practice/minor/': 'practice/practice.html',
            '/lessons_practice/sept/': 'practice/practice.html',
            '/lessons_practice/sus/': 'practice/practice.html',
            '/lessons_practice/minmaj/': 'practice/practice.html',
            '/lessons_practice/maj/': 'practice/practice.html',
        }

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)

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
