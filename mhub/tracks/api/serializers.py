from rest_framework import serializers

from tracks.models import Track


class TrackSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField('get_username_from_user')

    class Meta:
        model = Track
        fields = ['pk', 'name', 'description', 'username', 'audio_file', 'created_at', 'updated_at']

    def get_username_from_user(self, track):
        return track.user.username
