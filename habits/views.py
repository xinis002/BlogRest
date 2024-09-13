from rest_framework import viewsets, permissions
from .models import Habit
from .serializers import HabitSerializer
from rest_framework.pagination import PageNumberPagination

class HabitPagination(PageNumberPagination):
    page_size = 5

class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.action == 'list':
            return self.request.user.habits.all()
        return Habit.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

