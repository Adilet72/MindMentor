from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from ..serializers import UserSerializer
from django.contrib.auth import get_user_model

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
