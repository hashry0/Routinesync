from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Profile, Follow, Skill
from routine.models import Routine
class LandingPageView(TemplateView):
    def get(self, request):
        return render(request, "access/landing-page.html")

class HomepageView(TemplateView):
    def get(self, request):
        routine = Routine.objects.filter(author = request.user).order_by('-created_at').first()
        recent_routines = Routine.objects.filter(author = request.user).order_by('created_at')[:4]
        user = request.user
        return render(request, "access/homepage.html",context= {'user':user, 'routine':routine, 'recent_routines': recent_routines})

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
    def get(self, request, *args, **kwargs):
        username = Profile.objects.get(username = request.user.username)
        bar_username_profile = Profile.objects.get(username = kwargs['username'])
        is_following = Follow.objects.filter(user_following = username, user_followed = bar_username_profile).exists()
        following_count =  Follow.objects.filter(user_following = username).count()
        follower_count =  Follow.objects.filter(user_followed = username)
        return render (request, 'access/profile.html', context={'current_username':username, 
                                                                'profile_username': kwargs['username'],
                                                                 'is_following': is_following,
                                                                 'following_count': Follow.objects.filter(user_following = bar_username_profile).count(),
                                                                 'followers_count':Follow.objects.filter(user_followed = bar_username_profile).count(),
                                                                 'routines_count':Routine.objects.filter(author = bar_username_profile).count(),
                                                                 'skillsets': Skill.objects.filter(profile = bar_username_profile),
                                                                 'recent_routines': Routine.objects.filter(author = username).order_by("-created_at")[:3]})
