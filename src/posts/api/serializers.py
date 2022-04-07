from rest_framework import serializers

from posts.models import Post
from users.api.serializers import AccountPropertiesSerializer


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for Post model
    """

    user = serializers.SerializerMethodField('get_user_from_author')

    class Meta:
        model = Post
        fields = ['pk', 'title', 'content', 'user', 'created_at', 'updated_at']

    def get_user_from_author(self, post):
        return AccountPropertiesSerializer(post.author).data

