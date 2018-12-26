from .models import Room
import django_filters


class RoomFilter(django_filters.FilterSet):
	price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
	owner__username = django_filters.CharFilter(lookup_expr='icontains')
	address_line1 = django_filters.CharFilter(lookup_expr='icontains')
	town = django_filters.CharFilter(lookup_expr='icontains')
	furniture = django_filters.CharFilter(lookup_expr='icontains')
	description = django_filters.CharFilter(lookup_expr='icontains')
	class  Meta:
		model = Room 
		fields = ['town','price__lt','owner__username','description','furniture']
                