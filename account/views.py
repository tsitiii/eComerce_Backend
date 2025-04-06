from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, status
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from .models import User
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework.views import APIView
from django.utils.crypto import get_random_string
from django.urls import reverse
from django.conf import settings
from rest_framework.permissions import AllowAny


class PasswordResetConfirmView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, token):
        new_password = request.data.get('password')
        try:
            user = User.objects.get(reset_token=token)
            user.set_password(new_password)
            user.reset_token = ''
            user.save()
            return Response({'message': 'Password has been reset successfully.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        
        
class ResetPasswordView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            token = get_random_string(length=32)
            user.reset_token = token
            user.save()

            reset_link = f"http://localhost:5173/reset-password?token={token}"

            send_mail(
                'Password Reset Request',
                f'You can reset your password using the following link: {reset_link}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )

            return Response({'message': 'If this email exists, you will receive a reset email shortly.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message': 'Email not found'}, status=status.HTTP_400_BAD_REQUEST)



class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    