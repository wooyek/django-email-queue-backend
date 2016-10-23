# coding=utf-8
from django.core.mail.backends.base import BaseEmailBackend

from django_email_queue.models import QueuedEmailMessage


class EmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        message = QueuedEmailMessage.queue(email_messages)
        from django.conf import settings
        if settings.EMAIL_QUEUE_EAGER:
            message.send()
