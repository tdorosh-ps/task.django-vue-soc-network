from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post
from .serializers import PostRetrieveSerializer, PostCreateSerializer, PostListSerializer


class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.order_by('-created')
    serializer_class = PostListSerializer

    def get_queryset(self):
        owner = self.request.query_params.get('owner')
        if owner == 'true':
            return self.queryset.filter(owner=self.request.user)
        elif owner == 'false':
            return self.queryset.exclude(owner=self.request.user)
        return self.queryset.all()


@api_view(['POST'])
def post_like(request, pk):
    action = request.data.get('action')
    if action:
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'message': 'Post doesn\'t exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            if post.owner == request.user:
                return Response({'message': 'User can\'t like/unlike own posts'}, status=status.HTTP_400_BAD_REQUEST)
            if action == 'like':
                if request.user in post.users_liked.all():
                    return Response({'message': 'User already liked the post'}, status=status.HTTP_400_BAD_REQUEST)
                post.users_liked.add(request.user)
            elif action == 'unlike':
                if request.user not in post.users_liked.all():
                    return Response({'message': 'User didn\'t like the post'}, status=status.HTTP_400_BAD_REQUEST)
                post.users_liked.remove(request.user)
            return Response({'message': 'ok'}, status=status.HTTP_202_ACCEPTED)
    return Response({'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)


