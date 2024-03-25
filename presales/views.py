from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PresaleSerializer
from .models import Presale

class PresaleViewset(ModelViewSet):
    queryset = Presale.objects.all()
    serializer_class = PresaleSerializer
    lookup_field = "slug"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["chain"]
    