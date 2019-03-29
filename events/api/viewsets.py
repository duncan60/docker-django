from events.models import Campaign
from .serializers import CampaignSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    def list(self, request):
        queryset = Campaign.objects.all()
        serializer = CampaignSerializer(queryset, many=True)
        return Response({
          'success': True,
          'result': serializer.data
        })
