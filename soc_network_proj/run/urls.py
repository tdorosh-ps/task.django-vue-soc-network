from django.urls import path
from .views import run

urlpatterns = [
    path('', run),
]