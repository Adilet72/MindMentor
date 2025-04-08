from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed

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
