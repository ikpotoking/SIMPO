from django.urls import path

from rest_framework.routers import DefaultRouter


from .views import UserAPIViewSet,UserCreateAPIView


router = DefaultRouter()

router.register('users', UserAPIViewSet, basename='users')


urlpatterns = [
    path('create/',UserCreateAPIView.as_view(), name='create'),
    # path('users/', UserListAPIView.as_view(),name='users')
]

urlpatterns += router.urls
