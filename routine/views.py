from django.shortcuts import render, redirect
from django.views.generic import TemplateView
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
        return render(request, 'routine/routine_detail.html', context={'routine': routine})