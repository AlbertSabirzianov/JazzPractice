import shutil
import tempfile
from http import HTTPStatus

from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client, override_settings

from practice.models import Chord

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class LessonsUrlsTestCase(TestCase):
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
        cls.templates_name_urls = {
            '/lessons/all/': 'lessons/all.html',
            '/lessons/minor/': 'lessons/minor.html',
            '/lessons/sept/': 'lessons/sept.html',
            '/lessons/sus/': 'lessons/sus.html',
            '/lessons/half_diminished/': 'lessons/half_diminished.html',
            '/lessons/maj/': 'lessons/maj.html',
            '/lessons/minor_maj/': 'lessons/minor_maj.html',
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

    def test_redirect_url(self):
        """Проверка редиректов."""
        for adress in self.templates_name_urls.keys():
            with self.subTest(adress=adress):
                response = self.client.get(adress, follow=True)
                self.assertRedirects(response, f'/login/?next={adress}')
