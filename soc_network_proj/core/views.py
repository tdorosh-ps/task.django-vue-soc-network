from rest_framework import generics

from .models import User
from .serializers import UserCreateSerializer, UserRetrieveSerializer
from .tasks import clearbit_enrichment_task, hunter_verify_task


class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = []
    serializer_class = UserCreateSerializer

    # Delete unnecessary field from args and run celery tasks
    def perform_create(self, serializer):
        user = serializer.save()
        clearbit_enrichment_task.delay(user.id)
        hunter_verify_task.delay(user.id)


class UserRetrieveAPIView(generics.ListAPIView):
    serializer_class = UserRetrieveSerializer

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.id)
