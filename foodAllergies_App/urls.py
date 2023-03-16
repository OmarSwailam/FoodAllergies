from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework.authtoken import views
from django_rest_passwordreset.views import ResetPasswordValidateTokenViewSet, ResetPasswordConfirmViewSet, ResetPasswordRequestTokenViewSet



router = DefaultRouter()

router.register('users', UserViewSet, basename='Users')
router.register('VerifyEmail', VerifyEmail_viewSet, basename='VerifyEmail')

router.register('passwordreset_validate_token',ResetPasswordValidateTokenViewSet,basename='reset-password-validate')
router.register('passwordreset_confirm',ResetPasswordConfirmViewSet,basename='reset-password-confirm')
router.register('passwordreset',ResetPasswordRequestTokenViewSet,basename='reset-password-request')

urlpatterns = [
    path('login/', CustomAuthToken.as_view()),
    ]
urlpatterns = urlpatterns + router.urls