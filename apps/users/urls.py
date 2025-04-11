from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpecializationViewSet, ExperienceViewSet, AdminLoginView, AdminLogoutView, UserViewSet, \
    MentorCreateViewSet, BlockUserView, UnblockUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

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
    path('users/<int:user_id>/unblock/', UnblockUserView.as_view(), name='unblock_user'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
