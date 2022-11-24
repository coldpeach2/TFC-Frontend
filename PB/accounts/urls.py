from django.urls import path
from accounts.views import ProfileView, RegisterUserView, LoginView

app_name = 'accounts'

urlpatterns = [
    path('profile/', ProfileView.as_view()),
    path('register/', RegisterUserView.as_view()),
    #path('profile/update/', UpdateProfileView.as_view()),
    path('login/', LoginView.as_view())
] 