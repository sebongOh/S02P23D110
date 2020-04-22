from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.urls import path
from back import views
from back import models
from back.serializers import UsersSerializer
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
import back

# Serializers define the API representation.
# JSON형태로 변환해주는 라이브러리 Serializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # User모델안에 객체로 모두 가져와서 queryset 에 저장
    # queryset 은 모델형태

    serializer_class = UserSerializer
    # serializer_class 는 UserSerializer(JSON) 형태를 쓰겠다.


class UsersViewSet(viewsets.ModelViewSet):
    queryset = models.users.objects.all()
    serializer_class = UsersSerializer


    # Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'userlist', UsersViewSet)

# users 로 호출하면 UserViewSet 이 호출됨 13Line<<<<<<<<<<<<<<<

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('upload/', include('back.urls')),
    path('users/', views.join),
    path('login/', views.login),
    path('users/<int:pk>/', views.user_detail),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
