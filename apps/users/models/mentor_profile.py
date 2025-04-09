from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from core.models import BaseModel
from .user import User


class Specialization(BaseModel):
    title = models.CharField(
        max_length=100,
        verbose_name='Название',
        help_text='Название специализации, например, Python, Frontend, Backend.'
    )

    class Meta:
        db_table = 'specialization'
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

    def __str__(self):
        return self.title


class Experience(BaseModel):
    title = models.CharField(
        max_length=100,
        verbose_name='Название',
        help_text='Укажите уровень опыта работы, например, Junior, Middle, Senior.'
    )

    class Meta:
        db_table = 'experience'
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'

    def __str__(self):
        return self.title


class MentorProfile(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='mentor_profile',
        limit_choices_to={'role': 'mentor'},
        verbose_name='Пользователь',
        help_text='Связанный пользователь с ролью ментор.'
    )

    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Специализация',
        help_text='Выберите специализацию ментора из списка.'
    )

    experience = models.ForeignKey(
        Experience,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Опыт работы',
        help_text='Выберите уровень опыта работы ментора.'
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=0.00,
        validators=[MinValueValidator(0.00), MaxValueValidator(5.00)],
        verbose_name='Рейтинг',
        help_text='Рейтинг ментора от 0.00 до 5.00.'
    )

    reviews_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество отзывов',
        help_text='Количество оставленных отзывов.'
    )

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.specialization}, {self.experience})"

    class Meta:
        verbose_name = 'Профиль ментора'
        verbose_name_plural = 'Профили менторов'

