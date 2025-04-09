from django.contrib.auth import get_user_model
from django_filters import rest_framework as django_filters


class UserFilter(django_filters.FilterSet):
    role = django_filters.CharFilter(field_name='role', lookup_expr='exact', initial='user')

    class Meta:
        model = get_user_model()
        fields = ['role']