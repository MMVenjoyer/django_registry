from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Student
from .serializers import StudentSerializer


class StudentApiView(viewsets.ModelViewSet, APIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all() # Берем интересующие нас данные из подели при помощи метода
    serializer_class = StudentSerializer
