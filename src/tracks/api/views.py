from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import TrackSerializer
from tracks.models import Track


class TrackView(APIView):
    """
    List all tracks, or creates a new track.
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Lists all tracks.
        :param request:
        :return:
        """
        tracks = Track.objects.all()
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Creates a new track.
        """
        track = Track(user=request.user)

        serializer = TrackSerializer(track, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TrackDetailView(APIView):
    """
    Retrieve, update or delete a track instance.
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        """
        Retrieve the track instance.
        """
        try:
            return Track.objects.get(pk=pk)
        except Track.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        """
        Lists a track.
        """
        track = self.get_object(pk)
        serializer = TrackSerializer(track)
        if track:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """
        Updates a track.
        """
        track = self.get_object(pk)
        if track.user != request.user:
            data = {"error": "Request user is not the author of track"}
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
        serializer = TrackSerializer(track, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Deletes a track.
        """
        track = self.get_object(pk)

        if track.user != request.user:
            data = {"error": "Request user is not the author of track"}
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

        operation = track.delete()
        if operation:
            return Response({"Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"Delete failed"}, status=status.HTTP_400_BAD_REQUEST)
