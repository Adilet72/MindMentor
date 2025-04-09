from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from ..filters_func import MentorProfileFilter
from ..models import Specialization, Experience, MentorProfile
from ..permissions import IsAdmin
from ..serializers import SpecializationSerializer, ExperienceSerializer, MentorCreateSerializer
from django_filters.rest_framework import DjangoFilterBackend


class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class MentorCreateViewSet(viewsets.ModelViewSet):
    queryset = MentorProfile.objects.select_related('user')
    serializer_class = MentorCreateSerializer
    permission_classes = [IsAdmin]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MentorProfileFilter

