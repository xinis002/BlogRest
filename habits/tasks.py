from celery import shared_task
from habits.models import Habit
from telegram import Bot
from django.utils import timezone

bot = Bot(token='7398155814:AAHgy5Ak9tsSjxx9kA8i43-AKPxSsbWsX00')

@shared_task
def send_habit_reminders():
    habits = Habit.objects.filter(time__lte=timezone.now())
    for habit in habits:
        bot.send_message(chat_id=habit.user.telegram_chat_id, text=f"Reminder: {habit.action}")
