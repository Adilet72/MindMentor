from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from ..permissions import IsAdmin
from ..serializers import AdminLoginSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


class AdminLoginView(TokenObtainPairView):
    """
    Авторизация администратора. Возвращает access и refresh токены.
    """
    serializer_class = AdminLoginSerializer


class AdminLogoutView(APIView):
    """
    Выход администратора. Refresh токен добавляется в blacklist.
    """
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request):
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response({"detail": "Refresh токен обязателен."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Вы успешно вышли из системы."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"detail": "Ошибка при выходе из системы."}, status=status.HTTP_400_BAD_REQUEST)
