from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import TrackSerializer
from tracks.models import Track


class TrackList(APIView):
    """
    List all tracks, or creates a new track.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tracks = Track.objects.all()
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data)

    def post(self, request):

        track = Track(user=request.user)

        serializer = TrackSerializer(track, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TrackDetail(APIView):
    """
    Retrieve, update or delete a track instance.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Track.objects.get(pk=pk)
        except Track.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        track = self.get_object(pk)
        serializer = TrackSerializer(track)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        track = self.get_object(pk)

        if track.user != request.user:
            return Response({'Access forbidden'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = TrackSerializer(track, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        track = self.get_object(pk)

        if track.user != request.user:
            return Response({'Access forbidden'}, status=status.HTTP_401_UNAUTHORIZED)

        operation = track.delete()
        if operation:
            return Response({'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'Deletion failed'}, status=status.HTTP_400_BAD_REQUEST)