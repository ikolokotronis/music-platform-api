from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for Post model
    """

    username = serializers.SerializerMethodField('get_username_from_author')

    class Meta:
        model = Post
        fields = ['pk', 'title', 'content', 'username', 'created_at', 'updated_at']

    def get_username_from_author(self, post):
        return post.author.username

