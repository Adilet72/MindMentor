from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpecializationViewSet, ExperienceViewSet, AdminLoginView, AdminLogoutView, UserViewSet, \
    MentorCreateViewSet, BlockUserView, UnblockUserView

router = DefaultRouter()

router.register(r'specializations', SpecializationViewSet)
router.register(r'experiences', ExperienceViewSet)
router.register(r'users', UserViewSet)
router.register(r'mentors', MentorCreateViewSet, )


urlpatterns = [
    path('', include(router.urls)),
    path('admin/login/', AdminLoginView.as_view(), name='admin_login'),
    path('admin/logout/', AdminLogoutView.as_view(), name='admin_logout'),
    path('users/<int:user_id>/block/', BlockUserView.as_view(), name='block_user'),
    path('users/<int:user_id>/unblock/', UnblockUserView.as_view(), name='unblock_user')
]
