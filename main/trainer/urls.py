from django.urls import path, include
from rest_framework import routers

from .views import TrainerApiView


router = routers.DefaultRouter()
router.register(r'api/all', TrainerApiView)


urlpatterns = [
    path('Trainer/', include(router.urls)),
]