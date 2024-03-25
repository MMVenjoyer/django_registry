from rest_framework import serializers

from .models import Trainer


class TrainerSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    
    class Meta:
        model = Trainer
        fields = '__all__'