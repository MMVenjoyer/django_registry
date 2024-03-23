from django.urls import path, include
from rest_framework import routers

from .views import EstablishmentApiView


router = routers.DefaultRouter()
router.register(r'Establishment', EstablishmentApiView, basename='Establishment-detail')


urlpatterns = [
    path('api/v1/', include(router.urls)),
]