import django_filters
from ..models import MentorProfile

class MentorProfileFilter(django_filters.FilterSet):
    specialization = django_filters.CharFilter(field_name='specialization__name', lookup_expr='icontains')
    experience = django_filters.CharFilter(field_name='experience__name', lookup_expr='icontains')
    full_name = django_filters.CharFilter(method='filter_full_name')

    class Meta:
        model = MentorProfile
        fields = ['specialization', 'experience', 'full_name']

    def filter_full_name(self, queryset, name, value):
        return queryset.filter(
            user__first_name__icontains=value
        ) | queryset.filter(
            user__last_name__icontains=value
        )
