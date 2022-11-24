from django.urls import path
from .views import CreateStudioView, StudioView, ViewClosestStudiosView, ViewStudioView

app_name = 'studios'

urlpatterns = [
    path('add/', CreateStudioView.as_view()),
    path('<int:studio_id>/details/', StudioView.as_view()),
    path('closest_studios/', ViewClosestStudiosView.as_view()),
    path('<int:studio_id>/view/', ViewStudioView.as_view()),
]