from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timezone
from . import models

class CreateRoutineView(TemplateView):
    def get(self, request):
        routine_details = models.Todo.objects.filter(details__author = request.user)
        for detail in routine_details:
            print(f'Details {detail.details.title},')
        return render(request, "routine/create-routine.html", context={'routines': routine_details})

class EditRoutineView(TemplateView):
    def get(self, request, routine_slug):
        print(routine_slug)
        try:
            routine = models.Todo.objects.get(details__slug=routine_slug)
        except ObjectDoesNotExist:
            return redirect("homepage")
        else:
            return render (request, 'routine/edit-routine.html', context={'routine': routine})

class MyRoutinesView(TemplateView):
    def get(self, request):
        routines = models.Todo.objects.filter (details__author = request.user)
        return render(request, 'routine/my-routine.html', context={'routines': routines})
from django.core.exceptions import ObjectDoesNotExist
from . import models

class CreateRoutineView(TemplateView):
    def get(self, request):
        routine_details = models.Todo.objects.filter(details__author = request.user)
        for detail in routine_details:
            print(f'Details {detail.details.title},')
        return render(request, "routine/create-routine.html", context={'routines': routine_details})

class EditRoutineView(TemplateView):
    def get(self, request, routine_slug):
        print(routine_slug)
        try:
            routine = models.Todo.objects.get(details__slug=routine_slug)
        except ObjectDoesNotExist:
            return redirect("homepage")
        else:
            return render (request, 'routine/edit-routine.html', context={'routine': routine})

class MyRoutinesView(TemplateView):
    def get(self, request):
        routines = models.Todo.objects.filter (details__author = request.user)
        return render(request, 'routine/my-routine.html', context={'routines': routines})

class RoutineDetailView(TemplateView):
    def get(self, request, routine_slug):
        routine = models.Routine.objects.get(slug = routine_slug)
        tasks = models.Todo.objects.filter (details__slug = routine_slug)
        current_day = datetime.now()
        formatted_current_day = current_day.astimezone(timezone.utc)
        created_at = routine.created_at

        print(f'Current: {formatted_current_day}, Created at: {created_at}')
        routine_age = formatted_current_day - created_at
  
        if routine.privacy == True:
            priv_status = "Public"
        else: 
            priv_status = "Private"
        return render(request, 'routine/routine_detail.html', context={'routine': routine, 'tasks':tasks, 
        'privacy': priv_status , 'routine_age': routine_age.days})


class AddTaskView(TemplateView):
    def get(self, request, routine_slug):
        routine = models.Routine.objects.get(slug = routine_slug)
        return render (request, 'partials/add_task.html', context = {'routine': routine})