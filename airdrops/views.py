from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from airdrops.serializers import AirdropSerializer
from .models import Airdrop

class AirdropViewset(ModelViewSet):
    queryset = Airdrop.objects.all()
    serializer_class = AirdropSerializer
    lookup_field = "slug"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["categories__name"]
    