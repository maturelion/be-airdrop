from rest_framework.viewsets import ModelViewSet

from airdrops.serializers import AirdropSerializer
from .models import Airdrop

class AirdropViewset(ModelViewSet):
    queryset = Airdrop.objects.all()
    serializer_class = AirdropSerializer
    lookup_field = "id"
    