from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from .models import Establishment
from .serializers import EstablishmentSerializer


class EstablishmentApiView(viewsets.ModelViewSet):
    serializer_class = EstablishmentSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Establishment.objects.filter(owner_id=self.request.user.pk)
    

    def create(self, request, *args, **kwargs):
        establishment = Establishment.objects.filter(owner_id=self.request.user.pk)
        if establishment:
            serializer = EstablishmentSerializer(establishment, many=True)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
