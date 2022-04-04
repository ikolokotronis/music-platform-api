from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import TrackSerializer
from tracks.models import Track


class TrackList(APIView):
    """
    List all tracks, or create a new track.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tracks = Track.objects.all()
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data)

    def post(self, request):

        track = Track(artist=request.user)

        serializer = TrackSerializer(track, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)