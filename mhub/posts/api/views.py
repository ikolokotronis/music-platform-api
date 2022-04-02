from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from posts.models import Post
from users.models import Account
from .serializers import PostSerializer


class Api_Overview(APIView):
    def get(self, request):
        api_urls = {
            'All posts': 'GET /posts/',
            'Create post': 'POST /posts/',
            'View post': 'GET /posts/<str:pk>/',
            'Update post': 'POST /posts/<str:pk>/',
            'Delete post': 'DELETE /posts/<str:pk>/',
        }
        return Response(api_urls)


class PostView(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):

        account = Account.objects.get(id=1)

        post = Post(author=account)

        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        operation = post.delete()
        data = {}
        if operation:
            data['success'] = 'Delete successful'
            return Response(data=data, status=status.HTTP_200_OK)
        data['error'] = 'Delete failed'
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)
