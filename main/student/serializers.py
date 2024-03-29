from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    
    class Meta:
        model = Student
        fields = '__all__'