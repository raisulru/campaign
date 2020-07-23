from rest_framework import serializers
from .models import Campaign, Recipient, SentBox


class CampaginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = [
            'id',
            'campaign_title',
            'message_body',
            'status'
        ]


class RecipientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipient
        fields = [
            'id',
            'campaign',
            'recipient_number',
            'sender',
            'status'
        ]


class SentBoxSerializer(serializers.ModelSerializer):

    class Meta:
        model = SentBox
        fields = [
            'id',
            'campaign',
            'recipient_number',
            'create_time'
        ]


class RecipientPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipient
        fields = [
            'recipient_number',
            'sender',
        ]


class CampaginWithRecipientSerializer(serializers.Serializer):
    campaign_title = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    message_body = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    recipient_list = serializers.ListField(
        child=RecipientPostSerializer()
    )
