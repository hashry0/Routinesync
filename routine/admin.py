from django.contrib import admin
from .models import Routine, Todo, RoutineTracker

# Register your models here.

class RoutineAdmin(admin.ModelAdmin):
    list_display = ['get_author','title', 'created_at', 'updated_at','slug']

    def get_author(self, obj):
        return obj.author


class RoutineTrackerAdmin(admin.ModelAdmin):
    list_display = ["get_user", "get_routine"]

    def get_user(self, obj):
        return obj.user.username
    def get_routine(self, obj):
        return obj.routine.title

admin.site.register(Routine, RoutineAdmin)

class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_user', 'activity_name']

    def get_user(self, obj):
        return obj.details.author.username
admin.site.register(Todo, TodoAdmin)

admin.site.register(RoutineTracker, RoutineTrackerAdmin)
