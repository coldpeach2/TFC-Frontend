from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import routers
from accounts.views import ProfileView, RegisterUserView, LoginView, LogoutView
from studios.views import ViewClosestStudiosView, ViewStudioView


app_name = 'accounts'

#router = routers.SimpleRouter()
#router.register(r"profile", ProfileView)

urlpatterns = [
    path('profile/', ProfileView.as_view()),
    #path('', include(router.urls)),
    path('register/', RegisterUserView.as_view()),
    #path('profile/update/', UpdateProfileView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('closest_studios/', ViewClosestStudiosView.as_view()),
    path('<int:user_loc>/view/', ViewStudioView.as_view()),
] 