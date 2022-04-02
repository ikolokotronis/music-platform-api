from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
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
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class PostDetailView(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=404)

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=204)
