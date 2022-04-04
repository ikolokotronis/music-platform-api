from rest_framework import serializers

from tracks.models import Track


class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = ['name', 'description', 'audio_file', 'created_at', 'updated_at']


