from django.contrib.auth import get_user_model
from django_filters import rest_framework as django_filters

import django_filters
from django.contrib.auth import get_user_model

User = get_user_model()

class UserFilter(django_filters.FilterSet):
    role = django_filters.CharFilter(field_name='role', lookup_expr='exact', initial='user')
    first_name = django_filters.CharFilter(field_name='first_name', lookup_expr='icontains')
    last_name = django_filters.CharFilter(field_name='last_name', lookup_expr='icontains')
    email = django_filters.CharFilter(field_name='email', lookup_expr='icontains')
    phone = django_filters.CharFilter(field_name='phone', lookup_expr='icontains')
    is_blocked = django_filters.BooleanFilter(field_name='is_blocked')
    is_active = django_filters.BooleanFilter(field_name='is_active')
    created_at_after = django_filters.DateFilter(field_name='created_at', lookup_expr='gte', label='Created After')
    created_at_before = django_filters.DateFilter(field_name='created_at', lookup_expr='lte', label='Created Before')
    date_joined_after = django_filters.DateFilter(field_name='date_joined', lookup_expr='gte', label='Date Joined After')
    date_joined_before = django_filters.DateFilter(field_name='date_joined', lookup_expr='lte', label='Date Joined Before')

    class Meta:
        model = User
        fields = ['role', 'first_name', 'last_name', 'email', 'phone', 'is_blocked', 'is_active', 'date_joined', 'created_at']
