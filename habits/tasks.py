from celery import shared_task
from habits.models import Habit
from telegram import Bot
from django.utils import timezone
from config.settings import TELEGRAM_BOT_API_KEY

bot = Bot(TELEGRAM_BOT_API_KEY)

@shared_task
def send_habit_reminders():
    habits = Habit.objects.filter(time__lte=timezone.now())
    for habit in habits:
        if habit.user.telegram_chat_id:
            bot.send_message(chat_id=habit.user.telegram_chat_id, text=f"Напоминание: {habit.action}")
