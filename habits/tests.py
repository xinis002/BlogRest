from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from habits.models import Habit
from users.models import CustomUser
from habits.tasks import send_habit_reminders
from django.utils import timezone
from unittest.mock import patch, Mock


class HabitTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(email="test@example.com", username="testuser", password="password123")
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(user=self.user, place="Park", time="12:00", action="Run", execution_time=30)

    def test_create_habit(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "place": "Gym",
            "time": "15:00",
            "action": "Lift weights",
            "execution_time": 45,
            "pleasant_habit": False,
            "frequency": 1,
            "is_public": False
        }
        response = self.client.post(reverse('habit-list'), data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_habit_list(self):
        response = self.client.get(reverse('habit-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.habit.action)

    def test_get_habit_detail(self):
        response = self.client.get(reverse('habit-detail', kwargs={'pk': self.habit.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['action'], self.habit.action)

    def test_update_habit(self):
        data = {"action": "Jogging"}
        response = self.client.patch(reverse('habit-detail', kwargs={'pk': self.habit.id}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.habit.refresh_from_db()
        self.assertEqual(self.habit.action, "Jogging")


class HabitReminderTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email="test@example.com", username="testuser", password="password123")
        self.habit = Habit.objects.create(user=self.user, place="Park", time=timezone.now(), action="Run", execution_time=30)

    @patch('habits.tasks.Bot.send_message')
    def test_send_habit_reminders(self, mock_send_message):
        send_habit_reminders()
        mock_send_message.assert_called_once_with(chat_id=self.user.telegram_chat_id, text=f"Reminder: {self.habit.action}")

    @patch('habits.tasks.Bot.send_message', new_callable=Mock)
    def test_send_habit_reminders(self, mock_send_message):
        send_habit_reminders()
        mock_send_message.assert_called_once_with(chat_id=self.user.telegram_chat_id,
                                                  text=f"Reminder: {self.habit.action}")
