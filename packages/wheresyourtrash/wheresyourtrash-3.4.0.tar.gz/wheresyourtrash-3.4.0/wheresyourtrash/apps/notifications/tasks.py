from celery import shared_task
from django.core import management

@shared_task
def send_notifications():
    management.call_command('send_notifications')
