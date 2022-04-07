from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from posts.models import Post
from .serializers import PostSerializer


class PostView(APIView):
    def get(self, request):
        """
        Get all posts
        """
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create new post
        """
        authentication_classes = [TokenAuthentication]
        permission_classes = [IsAuthenticated]
        account = request.user

        post = Post(author=account)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    def get_object(self, pk):
        """
        Retrieve the post instance.
        """
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        """
        Get post
        """
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update post
        """
        post = self.get_object(pk)

        if post.author != request.user:
            return Response({'Access forbidden'}, status=status.HTTP_403_FORBIDDEN)

        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete post
        """
        post = self.get_object(pk)

        if post.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        operation = post.delete()
        data = {}
        if operation:
            data['success'] = 'Delete successful'
            return Response(data=data, status=status.HTTP_200_OK)
        data['error'] = 'Delete failed'
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)
