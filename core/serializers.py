from rest_framework import serializers

from core.models import Country, Language


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'alpha3', 'population',)


class NeighborSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='country-detail')

    class Meta:
        model = Country
        fields = ('name', 'url')


class CountryDetailsSerializer(serializers.ModelSerializer):
    languages = serializers.StringRelatedField(many=True)
    neighbors = NeighborSerializer(many=True)

    class Meta:
        model = Country
        fields = ('id', 'name', 'alpha2', 'alpha3', 'population', 'languages', 'neighbors',)
