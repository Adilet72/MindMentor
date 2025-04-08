from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, MentorProfile, Specialization, Experience
from django.contrib.auth.models import Group


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'role', 'phone', 'is_blocked', 'is_active', 'is_staff', 'date_joined', 'last_login')
    list_filter = ('role', 'is_active', 'is_blocked')
    search_fields = ('username', 'email', 'phone')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Личная информация', {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        ('Роль и статус', {'fields': ('role', 'is_blocked', 'is_active', 'is_staff')}),
        ('Прочее', {'fields': ('groups', 'user_permissions', 'last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        ('Личная информация', {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'phone'),
        }),
        ('Роль и статус', {
            'classes': ('wide',),
            'fields': ('role', 'is_blocked', 'is_active', 'is_staff'),
        }),
    )

    ordering = ('username',)


@admin.register(MentorProfile)
class MentorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'experience','rating','reviews_count', 'created_at', 'updated_at')
    list_filter = ('specialization', 'experience','rating')
    search_fields = ('user__username', 'user__email', 'specialization', 'experience')
    readonly_fields = ('created_at', 'updated_at','reviews_count','rating')
    fields = ('user', 'specialization', 'experience','rating','reviews_count', 'created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('title',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('title',)


admin.site.unregister(Group)
