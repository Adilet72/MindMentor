import uuid
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=6)

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email', 'role', 'phone', 'is_blocked',
            'is_active', 'date_joined', 'password','created_at',
        ]
        read_only_fields = ('is_active', 'date_joined','created_at',)

    def create(self, validated_data):
        password = validated_data.pop('password')

        if 'username' not in validated_data:
            validated_data['username'] = str(uuid.uuid4())[:30]

        validated_data.setdefault('role', 'user')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
