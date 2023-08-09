from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework import permissions, generics
from .serializers import RegisterSerializer, ResetPasswordSerializer
from .tasks import send_activation_email, send_confirmation_password_task
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import ActivationSerializer, GetActivationSerializer
from rest_framework.generics import GenericAPIView


User = get_user_model()


class RegistrationView(APIView):
    permission_classes = permissions.AllowAny,

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            try:
                result = send_activation_email.delay(user.email, user.activation_code)
            except:
                return Response({'message': 'Registered, but wasnt able to send activation code',
                                 'data': serializer.data}, status=201)

        return Response(serializer.data, status=201)


class ActivationView(GenericAPIView):
    permission_classes = permissions.AllowAny,
    serializer_class = ActivationSerializer

    def get(self, request):
        code = request.GET.get('u')
        user = get_object_or_404(User, activation_code=code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response('Успешно активирован', status=200)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Успешно активирован', status=200)


class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)


class LogoutView(APIView):
    permission_classes = permissions.IsAuthenticated,

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response('You logged out', status=205)
        except:
            return Response('Smth went wrong', status=400)


class UserDetailView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = permissions.IsAdminUser,


class UserProfileView(GenericAPIView):
    serializer_class = RegisterSerializer

    def get(self, request):
        user = request.user
        profile = get_object_or_404(User, email=user.email)
        serializer = RegisterSerializer(instance=profile)
        return Response(serializer.data, status=200)


class ResetPasswordView(APIView):
    def get(self, request):
        return Response({'message': 'Please provide an email to reset the password.'})

    def post(self, request):
        serializer = GetActivationSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
                user.create_activation_code()
                user.save()
                send_confirmation_password_task.delay(user.email, user.activation_code)
                return Response({'activation_code': user.activation_code}, status=200)
            except ObjectDoesNotExist:
                return Response({'message': 'User with this email does not exist.'}, status=404)
        return Response(serializer.errors, status=400)


class ResetPasswordConfirmView(APIView):
    def post(self, request):
        activation_code = request.GET.get('c')
        user = get_object_or_404(User, activation_code=activation_code)
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_password = serializer.validated_data['new_password']
        user.set_password(new_password)
        user.activation_code = ''
        user.save()
        return Response('Ваш пароль успешно обновлен', status=200)
