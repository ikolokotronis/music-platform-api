from django.test import TestCase, Client
from django.urls import reverse

from users.models import Account

client = Client()


class AccountViewTest(TestCase):
    def setUp(self):
        account = Account.objects.create(
            username="some_user", email="test_email@email.com"
        )
        account.set_password("some_password")
        account.save()

    def test_should_return_201_when_account_is_registered_with_right_data(self):
        data = {
            "username": "test_user",
            "email": "test_user@email.com",
            "password": "test_password",
            "password2": "test_password",
        }
        response = client.post(reverse("users:register"), data)
        actual_code = response.status_code
        expected_code = 201
        assert actual_code == expected_code

    def test_should_return_400_when_account_is_registered_with_wrong_password(self):
        data = {
            "username": "test_user",
            "email": "test_user@email.com",
            "password": "test_password",
            "password2": "test_password2",
        }
        response = client.post(reverse("users:register"), data)
        actual_code = response.status_code
        expected_code = 400
        assert actual_code == expected_code

    def test_should_return_200_when_user_is_logged_in_with_right_data(self):
        data = {"username": "some_user", "password": "some_password"}
        response = client.post(reverse("users:login"), data)
        actual_code = response.status_code
        expected_code = 200
        assert actual_code == expected_code

    def test_should_return_400_when_user_is_logged_in_with_wrong_password(self):
        data = {"username": "some_user", "password": "wrong_password"}
        response = client.post(reverse("users:login"), data)
        actual_code = response.status_code
        expected_code = 400
        assert actual_code == expected_code
