from django.test import TestCase, Client
from django.urls import reverse

from users.models import Account
from rest_framework.authtoken.models import Token


client = Client()


class MessageViewTest(TestCase):
    def setUp(self):
        account = Account.objects.create(
            username="test_user", email="test_email@email.com"
        )
        account.set_password("test_password")
        account.save()

        account2 = Account.objects.create(
            username="test_user2", email="test_email2@email.com"
        )
        account2.set_password("test_password2")
        account2.save()

    def test_should_return_201_when_sending_a_valid_message_to_other_user(self):
        account = Account.objects.get(username="test_user")
        token = Token.objects.get(user=account)
        key = token.key
        data = {"content": "some_content", "receiver": 1}
        response = client.post(
            reverse("conversations:messages"), data, HTTP_AUTHORIZATION=f"Token {key}"
        )
        actual_code = response.status_code
        expected_code = 201
        assert actual_code == expected_code

    def test_should_return_400_when_sending_a_message_to_not_existing_user(self):
        account = Account.objects.get(username="test_user")
        token = Token.objects.get(user=account)
        key = token.key
        data = {"content": "some_content", "receiver": 10}
        response = client.post(
            reverse("conversations:messages"), data, HTTP_AUTHORIZATION=f"Token {key}"
        )
        actual_code = response.status_code
        expected_code = 400
        assert actual_code == expected_code
