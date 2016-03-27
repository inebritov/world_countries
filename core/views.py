from core.models import Country
from core.serializers import CountryListSerializer, CountryDetailsSerializer
from rest_framework import filters
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination


class ParametrizedResultsSetPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class CountryList(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer
    pagination_class = ParametrizedResultsSetPagination

    filter_backends = (filters.OrderingFilter,)

    ordering_fields = ('name', 'population',)


class CountryDetail(RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailsSerializer
