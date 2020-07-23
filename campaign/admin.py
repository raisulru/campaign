from django.contrib import admin
from .models import Campaign, Recipient, SentBox


class CampaignAdmin(admin.ModelAdmin):
    list_display = ['campaign_title', 'message_body', 'status']
admin.site.register(Campaign, CampaignAdmin)


class RecipientsAdmin(admin.ModelAdmin):
    list_display = ['campaign', 'recipient_number', 'sender', 'status']
admin.site.register(Recipient, RecipientsAdmin)


class SentBoxAdmin(admin.ModelAdmin):
    list_display = ['campaign', 'recipient_number', 'create_time']
admin.site.register(SentBox, SentBoxAdmin)