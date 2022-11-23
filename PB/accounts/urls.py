from django.urls import path
from accounts.views import ProfileDetailUpdateView, RegisterUserView

app_name = 'accounts'

urlpatterns = [
    path('profile/', ProfileDetailUpdateView.as_view()),
    path('register/', RegisterUserView.as_view()),
] 