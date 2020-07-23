from django.urls import path

from .views import CampaignViewSet, RecipientViewSet, SentBoxViewSet, CampaignWithRecipientPostView


urlpatterns = [
    path('campaigns', CampaignViewSet.as_view({'get': 'list', 'post': 'create'}), name='campaign-list'),
    path('campaigns/<id>', CampaignViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='campaign-details'),
    path('create-campaign', CampaignWithRecipientPostView.as_view(), name='create-campaign-with-recipient')
]
