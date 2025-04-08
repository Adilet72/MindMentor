from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpecializationViewSet, ExperienceViewSet, AdminLoginView, AdminLogoutView

router = DefaultRouter()

router.register(r'specializations', SpecializationViewSet)
router.register(r'experiences', ExperienceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/login/', AdminLoginView.as_view(), name='admin_login'),
    path('admin/logout/', AdminLogoutView.as_view(), name='admin_logout'),
]
