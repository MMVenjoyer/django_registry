from django.urls import path, include
from rest_framework import routers

from .views import TrainerApiView


router = routers.DefaultRouter()
router.register(r'Trainer', TrainerApiView, basename='Trainer-detail')


urlpatterns = [
    path('api/v1/', include(router.urls)),
]