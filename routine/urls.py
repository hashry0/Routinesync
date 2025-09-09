from django.urls import path
from . import views

urlpatterns = [
    # path('routine/title/', api_views.RoutineTitleApiView.as_view(), name = 'routine_title'),
    path('routine/<slug:routine_slug>/', views.RoutineDetailView.as_view(), name = 'routine_detail'),
    path('edit/routine/<slug:routine_slug>/', views.EditRoutineView.as_view(), name = 'edit_routine'),
    path('create/routine/', views.CreateRoutineView.as_view(), name = 'create_routine'),
    path('my-routines/', views.MyRoutinesView.as_view(),  name = 'my_routines'),
    path('add-task/<slug:routine_slug>', views.AddTaskView.as_view(), name = 'add_task'),
]
