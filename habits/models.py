from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

User = get_user_model()

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')
    place = models.CharField(max_length=255)
    time = models.TimeField()
    action = models.CharField(max_length=255)
    pleasant_habit = models.BooleanField(default=False)
    related_habit = models.OneToOneField('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='dependent_habit')
    frequency = models.PositiveIntegerField(default=1)
    reward = models.CharField(max_length=255, blank=True, null=True)
    execution_time = models.PositiveIntegerField()
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.action} at {self.time} in {self.place}"

    def clean(self):
        if self.related_habit and self.reward:
            raise ValidationError("You can either set a related habit or a reward, but not both.")
        if self.execution_time > 120:
            raise ValidationError("Execution time cannot exceed 120 seconds.")
        if self.related_habit and not self.related_habit.pleasant_habit:
            raise ValidationError("Only pleasant habits can be set as related habits.")
        if self.frequency < 1 or self.frequency > 7:
            raise ValidationError("Habit must be performed at least once every 7 days.")

    class Meta:
        ordering = ['time']


