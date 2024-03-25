from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from main.permissions import IsVerified

from .models import Trainer
from .serializers import TrainerSerializer


class TrainerApiView(viewsets.ModelViewSet, APIView):
    permission_classes = [IsAuthenticated, IsVerified]
    serializer_class = TrainerSerializer


    def get_queryset(self):
        return Trainer.objects.filter(owner_id=self.request.user.pk)
