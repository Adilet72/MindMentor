from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers

class AdminLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        if user.role != 'admin':
            raise AuthenticationFailed('Доступ только для администраторов.')

        if not user.is_active or user.is_blocked:
            raise AuthenticationFailed('Пользователь заблокирован или неактивен.')

        data.update({
            'username': user.username,
            'email': user.email,
            'role': user.role,
        })

        return data


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()