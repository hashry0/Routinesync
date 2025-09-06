from django.urls import path
from . import api_views

urlpatterns = [
    path('routine/title/', api_views.RoutineTitleApiView.as_view(), name = 'routine_title_api'),
    path('create/routine/add/<slug:routine_slug>/', api_views.RoutineTaskAPIView.as_view(), name = 'add_routine_api'),
    path('routines/', api_views.RoutinesAPIView.as_view(), name = 'routines'),
    path('myroutines/', api_views.MyRoutinesAPIView.as_view(), name = 'my_routines'),
    path('tasks/<slug:routine_slug>/', api_views.TasksAPIView.as_view(), name = 'all_tasks'),
    path('edit/tasks/<slug:routine_slug>/', api_views.RoutineTaskAPIView.as_view(), name = 'edit_task_api'),
    path('edit/details/<slug:routine_slug>/', api_views.RoutineTitleApiView.as_view(), name = 'edit_routine_api'),
    path('edit/delete/<slug:routine_slug>/', api_views.DeleteRoutineApiView.as_view(), name = 'delete_routine_api'),
    path('privacy/<slug:routine_slug>/', api_views.PrivacyAPIView.as_view(), name='privacy_status'),
    path('routine/tracker/', api_views.RoutineTrackerAPIView.as_view(), name = "routine_tracker"),
    path('routine/tracker/<slug:routine_slug>/', api_views.RoutineTrackerAPIView.as_view(), name = "routine_tracker"),
]