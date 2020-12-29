from rest_framework import serializers

from .models import Post
from core.serializers import UserRetrieveSerializer


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body')


class PostRetrieveSerializer(serializers.ModelSerializer):
    users_liked = UserRetrieveSerializer(many=True)
    owner = UserRetrieveSerializer()

    class Meta:
        model = Post
        fields = ('id', 'owner', 'body', 'title', 'created', 'modified', 'users_liked')


class PostListSerializer(serializers.ModelSerializer):
    owner = UserRetrieveSerializer()
    users_liked_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'owner', 'title', 'created', 'modified', 'users_liked_count')

    def get_users_liked_count(self, obj):
        return obj.users_liked.count()