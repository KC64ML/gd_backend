

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from gdapp import views

router = routers.DefaultRouter()

router.register(r'communication', views.CommunicatewithpeopleViewSet)
router.register(r'diary', views.DiaryViewSet)
router.register(r'drugnotification', views.DrugnotificationViewSet)
router.register(r'game', views.GameViewSet)
router.register(r'location', views.LocationViewSet)
router.register(r'user', views.UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('account/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
