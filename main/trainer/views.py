from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Trainer
from .serializers import TrainerSerializer


class TrainerApiView(viewsets.ModelViewSet, APIView):
    permission_classes = [IsAuthenticated]
    queryset = Trainer.objects.all() # Берем интересующие нас данные из подели при помощи метода
    serializer_class = TrainerSerializer
