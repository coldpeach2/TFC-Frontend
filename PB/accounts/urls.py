from django.urls import path
from accounts.views import ProfileView, RegisterUserView, LoginView, LogoutView
from studios.views import ViewClosestStudiosView, ViewStudioView

app_name = 'accounts'

urlpatterns = [
    path('profile/', ProfileView.as_view()),
    path('register/', RegisterUserView.as_view()),
    #path('profile/update/', UpdateProfileView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('closest_studios/', ViewClosestStudiosView.as_view()),
    path('<int:studio_id>/view/', ViewStudioView.as_view()),
] 