from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from posts.models import PostModel
from posts.serializers import PostModelSerializers, UserSerializers
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model

User = get_user_model()


class PostViewSetApi(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializers


class UserViewSetApi(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializers


def index(request):
    return render(request, "api_list.html")





