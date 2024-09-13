from rest_framework import serializers
from .models import Habit

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def validate(self, data):
        if data.get('related_habit') and data.get('reward'):
            raise serializers.ValidationError("Cannot have both a related habit and a reward.")
        if data.get('execution_time') is not None and data.get('execution_time') > 120:
            raise serializers.ValidationError("Execution time cannot exceed 120 seconds.")
        return data
