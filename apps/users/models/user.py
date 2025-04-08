from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        """
        Создание обычного пользователя.
        """
        if not username:
            raise ValueError('Пользователь должен иметь имя пользователя')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        """
        Создание суперпользователя с ролью "admin".
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 'admin')  # Устанавливаем роль админа

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    class Role(models.TextChoices):
        USER = 'user', 'Пользователь'
        MENTOR = 'mentor', 'Ментор'
        ADMIN = 'admin', 'Админ'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER,
        verbose_name='Роль',
        help_text='Выберите роль пользователя: обычный пользователь, ментор или администратор.'
    )

    phone = models.CharField(
        max_length=20,
        verbose_name='Телефон',
        blank=True,
        null=True,
        help_text='Введите номер телефона в формате +7 (XXX) XXX-XX-XX (опционально).'
    )

    is_blocked = models.BooleanField(
        default=False,
        verbose_name='Заблокирован',
        help_text='Если включено, пользователь не сможет войти в систему.'
    )

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
