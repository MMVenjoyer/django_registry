from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Student
from .serializers import StudentSerializer


class StudentApiView(viewsets.ModelViewSet, APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer


    def get_queryset(self):
        return Student.objects.filter(owner_id=self.request.user.pk)
