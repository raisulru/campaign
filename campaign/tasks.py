from celery import shared_task
from .models import SentBox

# @shared_task
def sent_to_sentbox(campaign, number):
    sent_box = SentBox(
        campaign_id=campaign,
        recipient_number=number
    )

    sent_box.save()