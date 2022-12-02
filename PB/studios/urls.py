from django.urls import path
from .views import ViewStudioView, StudiosForUserView, StudioClassScheduleView, UserStudioSearch, UserClassSearch, \
    EnrolUserView, UserScheduleView

app_name = 'studios'

urlpatterns = [
    path('<int:studio_id>/view/', ViewStudioView.as_view()),
    path('all/', StudiosForUserView.as_view()),
    path('<int:id>/classes/', StudioClassScheduleView.as_view()),
    path('studio/search/', UserStudioSearch.as_view()),
    path('classes/search/', UserClassSearch.as_view()),
    path('<int:studio_id>/<int:class_id>/enrol/', EnrolUserView.as_view()),
    path('my_schedule/', UserScheduleView.as_view()),
]