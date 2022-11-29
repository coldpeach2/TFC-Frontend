from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import routers
from .views import ProfileView, RegisterUserView, LoginView, LogoutView, ActivateUserSubscriptionView


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
    path('subscribe/', ActivateUserSubscriptionView.as_view())
] 