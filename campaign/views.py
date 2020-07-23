from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Campaign, Recipient, SentBox
from .serializers import CampaginSerializer, RecipientSerializer, SentBoxSerializer, CampaginWithRecipientSerializer
from .tasks import sent_to_sentbox


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaginSerializer
    lookup_field = 'id'


class RecipientViewSet(viewsets.ModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer
    lookup_field = 'id'


class SentBoxViewSet(viewsets.ModelViewSet):
    queryset = SentBox.objects.all()
    serializer_class = SentBoxSerializer
    lookup_field = 'id'


class CampaignWithRecipientPostView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = CampaginWithRecipientSerializer(data=request.data)
        
        if serializer.is_valid():
            campaign_data = {
                'campaign_title': serializer.data.get('campaign_title'),
                'message_body': serializer.data.get('message_body')
            }

            recipient_data = serializer.data.get('recipient_list')

            campaign_serializer = CampaginSerializer(data=campaign_data)

            if campaign_serializer.is_valid():
                campaign_obj = campaign_serializer.save()

                for item in recipient_data:
                    recipient = Recipient(
                        recipient_number=item.get('recipient_number'),
                        sender=item.get('sender'),
                        campaign=campaign_obj
                    )
                    recipient.save()

                return Response(campaign_serializer.data, 201)
            return Response(campaign_serializer.errors, 400)
        return Response(serializer.errors, 400)


class SentToSentBoxView(APIView):

    def post(self, request, *args, **kwargs):
        campaign_id = kwargs.get('campaign_id')

        recipient_list = Recipient.objects.filter(campaign__id=campaign_id)
        for recipient in recipient_list:
            sent_to_sentbox(campaign_id, recipient.recipient_number)
        return Response({'msg': 'Message sending start'}, 200)