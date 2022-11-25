from django.urls import path
from classes.views import ClassScheduleViewAPI

app_name = 'classes'

urlpatterns = [
    path('classes/', ClassScheduleViewAPI.as_view()),
] 