from rest_framework import serializers
from .models import Presale


class PresaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Presale
        fields = (
            'url',
            'id',
            'name',
            'slug',
            'logo',
            'chain',
            'price',
            'quantity',
            'start_date',
            'end_date',
            'date_added'
        )
        extra_kwargs = {
            "url": {"view_name": "presale-detail", "lookup_field": "slug"}}
