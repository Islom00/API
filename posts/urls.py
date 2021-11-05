from django.urls import path
from rest_framework.routers import SimpleRouter

from posts.views import UserViewSetApi, PostViewSetApi

router = SimpleRouter()
router.register("users", UserViewSetApi, basename="users")
router.register("posts", PostViewSetApi, basename="posts")

urlpatterns = router.urls
