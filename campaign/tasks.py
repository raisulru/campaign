from celery import shared_task
from .models import Campaign, Recipient, SentBox

@shared_task
def sent_to_sentbox(recipient):
    sent_box = SentBox(
        campaign=recipient.campaign,
        recipient_number=recipient.recipient_number
    )

    sent_box.save()