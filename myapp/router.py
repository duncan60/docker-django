from events.api.viewsets import CampaignViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('events', CampaignViewSet, base_name='events')
# for url in router.urls:
#     print(url, '\n')
