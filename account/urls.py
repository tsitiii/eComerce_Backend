from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'account'

router = DefaultRouter()
router.register('register', RegisterViewSet, basename='register')

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='token_obtain_pair'),  # Use custom view
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('reset-password-confirm/<str:token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('', include(router.urls)),
]