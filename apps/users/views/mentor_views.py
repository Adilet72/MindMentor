from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from ..filters_func import MentorProfileFilter
from ..models import Specialization, Experience,MentorProfile
from ..permissions import IsAdmin
from ..serializers import SpecializationSerializer, ExperienceSerializer,MentorCreateSerializer
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class  MentorCreateViewSet(viewsets.ModelViewSet):
    queryset = MentorProfile.objects.all()
    serializer_class = MentorCreateSerializer
    permission_classes = [IsAdmin]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MentorProfileFilter

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('specialization', openapi.IN_QUERY, description="Фильтрация по специализации", type=openapi.TYPE_INTEGER),
        openapi.Parameter('experience', openapi.IN_QUERY, description="Фильтрация по опыту", type=openapi.TYPE_INTEGER),
        openapi.Parameter('full_name', openapi.IN_QUERY, description="Фильтрация по полному имени", type=openapi.TYPE_STRING),
        openapi.Parameter('rating_min', openapi.IN_QUERY, description="Минимальный рейтинг", type=openapi.TYPE_INTEGER),
        openapi.Parameter('rating_max', openapi.IN_QUERY, description="Максимальный рейтинг", type=openapi.TYPE_INTEGER),
        openapi.Parameter('reviews_count_min', openapi.IN_QUERY, description="Мин. количество отзывов", type=openapi.TYPE_INTEGER),
        openapi.Parameter('reviews_count_max', openapi.IN_QUERY, description="Макс. количество отзывов", type=openapi.TYPE_INTEGER),
        openapi.Parameter('created_at_after', openapi.IN_QUERY, description="Создано после", type=openapi.TYPE_STRING, format='date'),
        openapi.Parameter('created_at_before', openapi.IN_QUERY, description="Создано до", type=openapi.TYPE_STRING, format='date'),
        openapi.Parameter('email', openapi.IN_QUERY, description="Фильтрация по email", type=openapi.TYPE_STRING),
        openapi.Parameter('role', openapi.IN_QUERY, description="Фильтрация по роли", type=openapi.TYPE_STRING),
        openapi.Parameter('phone', openapi.IN_QUERY, description="Фильтрация по телефону", type=openapi.TYPE_STRING),
        openapi.Parameter('is_blocked', openapi.IN_QUERY, description="Заблокирован", type=openapi.TYPE_BOOLEAN),
        openapi.Parameter('is_active', openapi.IN_QUERY, description="Активен", type=openapi.TYPE_BOOLEAN),
        openapi.Parameter('date_joined_after', openapi.IN_QUERY, description="Дата регистрации после", type=openapi.TYPE_STRING, format='date'),
        openapi.Parameter('date_joined_before', openapi.IN_QUERY, description="Дата регистрации до", type=openapi.TYPE_STRING, format='date'),
    ])
    def list(self, request, *args, **kwargs):

        return super().list(request, *args, **kwargs)