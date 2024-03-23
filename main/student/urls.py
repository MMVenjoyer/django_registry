from django.urls import path, include
from rest_framework import routers

from .views import StudentApiView


router = routers.DefaultRouter()
router.register(r'api/all', StudentApiView)


urlpatterns = [
    path('Student/', include(router.urls)),
]