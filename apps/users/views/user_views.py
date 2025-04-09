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


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserFilter
    queryset = get_user_model().objects.all()



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