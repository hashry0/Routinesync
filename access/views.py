from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Profile
from routine.models import Routine
class LandingPageView(TemplateView):
    def get(self, request):
        return render(request, "access/landing-page.html")

class HomepageView(TemplateView):
    def get(self, request):
        routine = Routine.objects.filter(author = request.user).order_by('-created_at').first()
        user = request.user
        return render(request, "access/homepage.html",context= {'user':user, 'routine':routine})

class RegisterView(TemplateView):
    def get(self, request):
        return render(request, "access/registration.html")


class LoginView(TemplateView):
    def get(self, request):
        return render(request, "access/log-in.html")

class GenderView(TemplateView):
    def get(self, request):
        gender_choice = Profile.gender_choice
        return render(
            request, "access/partials/gender-choice.html", {"gender_choice": gender_choice})

class ProfileView(TemplateView):
    def get(self, request):
        return render (request, 'access/profile.html')

