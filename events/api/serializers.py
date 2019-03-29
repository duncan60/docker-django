from rest_framework import serializers
from events.models import Campaign

class CampaignSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Campaign
        fields = ('name', 'pub_date')
