from django.urls import path
from .views import CreateStudioView, StudioView, ViewClosestStudiosView, ViewStudioView, StudiosForUserView, StudioClassScheduleView

app_name = 'studios'

urlpatterns = [
    path('add/', CreateStudioView.as_view()),
    path('<int:studio_id>/details/', StudioView.as_view()),
    path('closest_studios/', ViewClosestStudiosView.as_view()),
    path('<int:studio_id>/view/', ViewStudioView.as_view()),
    path('all/', StudiosForUserView.as_view()),
    path('<int:id>/classes/', StudioClassScheduleView.as_view()),

]