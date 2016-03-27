from rest_framework import serializers

from core.models import Country


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'alpha3', 'population',)


class CountryDetailsSerializer(serializers.ModelSerializer):
    languages = serializers.StringRelatedField(many=True)
    neighbors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Country
        fields = ('id', 'name', 'alpha2', 'alpha3', 'population', 'languages', 'neighbors',)
