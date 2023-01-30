from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import routers
from .views import ProfileView, RegisterUserView, LoginView, LogoutView, ActivateUserSubscriptionView, UpdateAccountView, ProfileUpdateView, PaymentHistoryView


app_name = 'accounts'


urlpatterns = [
    path('profile/', ProfileView.as_view()),
    path('register/', RegisterUserView.as_view()),
    path('profile/update/', ProfileUpdateView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/logout/', LogoutView.as_view()),
    path('profile/subscribe/', ActivateUserSubscriptionView.as_view()), 
    path('profile/subscribe/update/', UpdateAccountView.as_view()),
    path('profile/history/', PaymentHistoryView.as_view())
] 