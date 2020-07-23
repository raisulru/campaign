from django.db import models
from .enums import (
    CAMPAIGN_STATUS, 
    PENDING, 
    SENDER_CHOICES,
    RECIPIENT_STATUS
)


class Campaign(models.Model):
    campaign_title = models.CharField(max_length=150)
    message_body = models.TextField()
    status = models.CharField(max_length=50, choices=CAMPAIGN_STATUS, default=PENDING)

    def __str__(self):
        return self.campaign_title

    class Meta:
        db_table = 'campaigns'
        verbose_name = 'Campaign'
        verbose_name_plural = 'Campaigns'


class Recipient(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='recipients')
    recipient_number = models.CharField(max_length=20)
    sender = models.CharField(max_length=2, choices=SENDER_CHOICES)
    status = models.CharField(max_length=20, choices=RECIPIENT_STATUS, default=PENDING)

    def __str__(self):
        return self.recipient_number

    class Meta:
        db_table = 'recipients'
        verbose_name = 'Recipient'
        verbose_name_plural = 'Recipients'


class SentBox(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.DO_NOTHING, related_name='sent_itms')
    recipient_number = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.campaign.campaign_title

    class Meta:
        db_table = 'sent_box'
        verbose_name = 'Sent Box'
        verbose_name_plural = 'Sent Boxes'