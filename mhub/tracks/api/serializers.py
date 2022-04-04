from rest_framework import serializers

from tracks.models import Track


class TrackSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField('get_username_from_author')

    class Meta:
        model = Track
        fields = ['name', 'description', 'username', 'audio_file', 'created_at', 'updated_at']

    def get_username_from_author(self, track):
        return track.user.username
