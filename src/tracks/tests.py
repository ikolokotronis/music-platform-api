from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from users.models import Account
from rest_framework.authtoken.models import Token

client = Client()


class TrackViewTest(TestCase):
    def setUp(self):
        account = Account.objects.create(
            username="test_user", email="test_email@email.com"
        )
        account.set_password("test_password")
        account.save()

    def test_should_return_201_when_adding_a_track_as_user(self):
        account = Account.objects.get(username="test_user")
        token = Token.objects.get(user=account)
        key = token.key
        data = {
            "name": "some_name",
            "description": "some_description",
            "user": 0,
            "audio_file": SimpleUploadedFile(
                "some_audio_file.mp3", b"audio_file_content"
            ),
            "img_file": SimpleUploadedFile("some_img_file.png", b"img_file_content"),
        }
        response = client.post(
            reverse("tracks:track_view"), data, HTTP_AUTHORIZATION=f"Token {key}"
        )
        actual_code = response.status_code
        expected_code = 201
        assert actual_code == expected_code

    def test_should_return_400_when_adding_a_track_without_audio_file(self):
        account = Account.objects.get(username="test_user")
        token = Token.objects.get(user=account)
        key = token.key
        data = {
            "name": "some_name",
            "description": "some_description",
            "user": 0,
            "img_file": SimpleUploadedFile("some_img_file.png", b"img_file_content"),
        }
        response = client.post(
            reverse("tracks:track_view"), data, HTTP_AUTHORIZATION=f"Token {key}"
        )
        actual_code = response.status_code
        expected_code = 400
        assert actual_code == expected_code
