import django_filters
from ..models import MentorProfile


class MentorProfileFilter(django_filters.FilterSet):
    specialization = django_filters.NumberFilter(field_name='specialization__id', lookup_expr='exact')  # Фильтрация по ID
    experience = django_filters.NumberFilter(field_name='experience__id', lookup_expr='exact')  # Фильтрация по ID
    full_name = django_filters.CharFilter(method='filter_full_name')
    rating_min = django_filters.NumberFilter(field_name='rating', lookup_expr='gte', label='Min Rating')  # Минимальный рейтинг
    rating_max = django_filters.NumberFilter(field_name='rating', lookup_expr='lte', label='Max Rating')  # Максимальный рейтинг
    reviews_count_min = django_filters.NumberFilter(field_name='reviews_count', lookup_expr='gte', label='Min Reviews Count')  # Мин. количество отзывов
    reviews_count_max = django_filters.NumberFilter(field_name='reviews_count', lookup_expr='lte', label='Max Reviews Count')  # Макс. количество отзывов
    created_at_after = django_filters.DateFilter(field_name='created_at', lookup_expr='gte', label='Created After')  # После какой даты
    created_at_before = django_filters.DateFilter(field_name='created_at', lookup_expr='lte', label='Created Before')  # До какой даты

    class Meta:
        model = MentorProfile
        fields = ['specialization', 'experience', 'full_name', 'rating_min', 'rating_max', 'reviews_count_min', 'reviews_count_max', 'created_at_after', 'created_at_before']

    def filter_full_name(self, queryset, name, value):
        return queryset.filter(user__first_name__icontains=value) | queryset.filter(user__last_name__icontains=value)
