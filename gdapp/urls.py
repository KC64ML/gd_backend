from django.urls import path, include
from rest_framework import routers
from gdapp.views import UserViewSet

urlpatterns = [
    path("", include("gdapp.oauth.urls")),
]

router = routers.DefaultRouter()
router.register(r"user", UserViewSet)

urlpatterns += router.urls
