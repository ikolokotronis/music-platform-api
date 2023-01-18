from django.test import TestCase, Client
from django.urls import reverse

client = Client()


class PostViewTest(TestCase):
    def test_should_return_401_when_auth_token_is_not_provided(self):
        response = client.get(reverse("posts:post_view"))
        actual_code = response.status_code
        expected_code = 401
        assert actual_code == expected_code
