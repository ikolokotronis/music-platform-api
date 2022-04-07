from rest_framework import serializers

from tracks.models import Track
from users.api.serializers import AccountPropertiesSerializer


class TrackSerializer(serializers.ModelSerializer):
    """
    Serializer for Track model
    """

    user = serializers.SerializerMethodField('get_user')

    class Meta:
        model = Track
        fields = ['pk', 'name', 'description', 'user', 'audio_file', 'img_file',  'created_at', 'updated_at']

    def get_user(self, track):
        return AccountPropertiesSerializer(track.user).data
