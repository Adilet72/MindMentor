from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from ..filters_func import UserFilter
from ..models import User
from ..permissions import IsAdmin
from ..serializers import UserSerializer,UserBlockSerializer
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserFilter
    queryset = get_user_model().objects.all()

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('role', openapi.IN_QUERY, description="Фильтр по роли", type=openapi.TYPE_STRING),
        openapi.Parameter('first_name', openapi.IN_QUERY, description="Фильтр по имени", type=openapi.TYPE_STRING),
        openapi.Parameter('last_name', openapi.IN_QUERY, description="Фильтр по фамилии", type=openapi.TYPE_STRING),
        openapi.Parameter('email', openapi.IN_QUERY, description="Фильтр по email", type=openapi.TYPE_STRING),
        openapi.Parameter('phone', openapi.IN_QUERY, description="Фильтр по телефону", type=openapi.TYPE_STRING),
        openapi.Parameter('is_blocked', openapi.IN_QUERY, description="Заблокирован", type=openapi.TYPE_BOOLEAN),
        openapi.Parameter('is_active', openapi.IN_QUERY, description="Активен", type=openapi.TYPE_BOOLEAN),
        openapi.Parameter('created_at_after', openapi.IN_QUERY, description="Создан после", type=openapi.TYPE_STRING, format='date'),
        openapi.Parameter('created_at_before', openapi.IN_QUERY, description="Создан до", type=openapi.TYPE_STRING, format='date'),
        openapi.Parameter('date_joined_after', openapi.IN_QUERY, description="Дата регистрации после", type=openapi.TYPE_STRING, format='date'),
        openapi.Parameter('date_joined_before', openapi.IN_QUERY, description="Дата регистрации до", type=openapi.TYPE_STRING, format='date'),
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)



class BlockUserView(APIView):
    def patch(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'detail': 'Пользователь не найден.'}, status=status.HTTP_404_NOT_FOUND)

        # Устанавливаем статус заблокированного пользователя
        user.is_blocked = True
        user.save()

        return Response({'detail': 'Пользователь заблокирован.'}, status=status.HTTP_200_OK)

class UnblockUserView(APIView):
    def patch(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'detail': 'Пользователь не найден.'}, status=status.HTTP_404_NOT_FOUND)
        user.is_blocked = False
        user.save()

        return Response({'detail': 'Пользователь разблокирован.'}, status=status.HTTP_200_OK)