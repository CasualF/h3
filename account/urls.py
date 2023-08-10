from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from .views import ResetPasswordView, ResetPasswordConfirmView

urlpatterns = [
    path('register/', views.RegistrationView.as_view()),
    path('activate/', views.ActivationView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('', views.UserDetailView.as_view()),
    path('profile/', views.UserProfileView.as_view()),
    path('reset-password/', ResetPasswordView.as_view()),
    path('reset-password/confirm/', ResetPasswordConfirmView.as_view()),
]

