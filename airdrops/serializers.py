from rest_framework import serializers
from .models import Airdrop, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class AirdropSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Airdrop
        fields = '__all__'

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        airdrop = Airdrop.objects.create(**validated_data)
        for category_data in categories_data:
            category, _ = Category.objects.get_or_create(**category_data)
            airdrop.categories.add(category)
        return airdrop

    def update(self, instance, validated_data):
        categories_data = validated_data.pop('categories')
        instance = super().update(instance, validated_data)
        instance.categories.clear()
        for category_data in categories_data:
            category, _ = Category.objects.get_or_create(**category_data)
            instance.categories.add(category)
        return instance
