from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import MentorProfile, Specialization, Experience
import uuid

User = get_user_model()


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['id', 'title']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'title']


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=6)

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email', 'role', 'phone', 'is_blocked',
            'is_active', 'date_joined', 'password'
        ]
        read_only_fields = ('is_active', 'date_joined')

    def create(self, validated_data):
        password = validated_data.pop('password')
        if 'username' not in validated_data:
            validated_data['username'] = str(uuid.uuid4())[:30]
        validated_data.setdefault('role', 'mentor')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user


class MentorCreateSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()  # Используем UserCreateSerializer для создания пользователя
    specialization = serializers.PrimaryKeyRelatedField(queryset=Specialization.objects.all())
    experience = serializers.PrimaryKeyRelatedField(queryset=Experience.objects.all())

    class Meta:
        model = MentorProfile
        fields = [
            'id','user', 'specialization', 'experience','rating','reviews_count','created_at'
        ]
        read_only_fields = ('rating','reviews_count','created_at')



    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserCreateSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        mentor_profile = MentorProfile.objects.create(
            user=user,
            **validated_data
        )

        return mentor_profile

"""
{
  "user": {
    "first_name": "Айнура",
    "last_name": "Калыкова",
    "email": "aynurfgdfgaa@example.com",
    "phone": "+996700112233",
    "password": "supersecret123"
  },
  "specialization": 1,
  "experience": 2
}
"""