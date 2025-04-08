from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from ..permissions import IsAdmin
from ..serializers import UserSerializer
from django.contrib.auth import get_user_model
from django_filters import rest_framework as django_filters


class UserFilter(django_filters.FilterSet):
    role = django_filters.CharFilter(field_name='role', lookup_expr='exact', initial='user')

    class Meta:
        model = get_user_model()
        fields = ['role']


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserFilter
    queryset = get_user_model().objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(role='user')