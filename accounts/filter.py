from django_filters.filters import DateFilter
from accounts.models import Order
import django_filters
class OrderFilter(django_filters.FilterSet):
    start_date=DateFilter(field_name='created_at',lookup_expr='gte')
    class Meta:
        model=Order
        fields='__all__'
        exclude=['customer','created_at']