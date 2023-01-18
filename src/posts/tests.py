from django.test import TestCase, Client
from django.urls import reverse

from posts.models import Post
from users.models import Account
from rest_framework.authtoken.models import Token

client = Client()


class PostViewTest(TestCase):
    def setUp(self):
        account = Account.objects.create(
            username="test_user", email="test_email@email.com"
        )
        account.set_password("test_password")
        account.save()

        Post.objects.create(title="test title", content="test content", author=account)

    def test_should_return_401_when_auth_token_is_not_provided(self):
        response = client.get(reverse("posts:post_view"))
        actual_code = response.status_code
        expected_code = 401
        assert actual_code == expected_code

    def test_should_return_200_when_viewing_all_posts_as_user(self):
        account = Account.objects.get(username="test_user")
        token = Token.objects.get(user=account)
        key = token.key
        response = client.get(
            reverse("posts:post_view"), HTTP_AUTHORIZATION=f"Token {key}"
        )
        actual_code = response.status_code
        expected_code = 200
        assert actual_code == expected_code

    def test_should_return_200_when_viewing_detailed_post_as_user(self):
        account = Account.objects.get(username="test_user")
        token = Token.objects.get(user=account)
        key = token.key
        response = client.get(
            reverse("posts:post_detail", kwargs={"pk": 1}),
            HTTP_AUTHORIZATION=f"Token {key}",
        )
        actual_code = response.status_code
        expected_code = 200
        print(actual_code)
        assert actual_code == expected_code
