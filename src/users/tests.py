from django.test import TestCase, Client
from django.urls import reverse

client = Client()


class AccountRegisterTest(TestCase):
    def test_should_return_200_when_account_is_registered_with_right_data(self):
        data = {
            "username": "test_user",
            "email": "test_user@email.com",
            "password": "test_password",
            "password2": "test_password",
        }
        response = client.post(reverse("users:register"), data)
        actual_code = response.status_code
        expected_code = 200
        assert actual_code == expected_code

    def test_should_return_404_when_account_is_registered_with_wrong_data(self):
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
