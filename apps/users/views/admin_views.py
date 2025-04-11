from rest_framework_simplejwt.views import TokenObtainPairView
from ..permissions import IsAdmin
from ..serializers import AdminLoginSerializer, LogoutSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

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

    @swagger_auto_schema(
        request_body=LogoutSerializer,
        responses={
            205: openapi.Response("Вы успешно вышли из системы."),
            400: openapi.Response("Ошибка при выходе из системы.")
        }
    )
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        refresh_token = serializer.validated_data["refresh"]

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Вы успешно вышли из системы."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"detail": "Ошибка при выходе из системы."}, status=status.HTTP_400_BAD_REQUEST)