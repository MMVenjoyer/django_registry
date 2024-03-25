from django.urls import path, include
from rest_framework import routers

from .views import StudentApiView


router = routers.DefaultRouter()
router.register(r'Student', StudentApiView, basename='Student-detail')


urlpatterns = [
    path('api/v1/', include(router.urls)),
]