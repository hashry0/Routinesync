from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Routine, Todo, RoutineTracker
from django.core.exceptions import ObjectDoesNotExist
from . import serializers
import requests
from common import permissions
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.
class RoutineTitleApiView(APIView):
    permission_classes =[permissions.AccessPermission]
    def post(self, request):
        routine_details_serializer = serializers.RoutineSerializer(data = request.data, context = {'request': request})
        if routine_details_serializer.is_valid():
            routine_details_serializer.save()
            return Response({"message": routine_details_serializer.data,}, status=status.HTTP_201_CREATED)
        return Response({"message":routine_details_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, routine_slug):
        try:
            get_routine_details = Routine.objects.get(slug=routine_slug)
        except ObjectDoesNotExist:
            return Response({'message': "Routine can't be found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            if request.user != get_routine_details.author:
                return Response({'message':'This can only be edited by the owner'},  status=status.HTTP_403_FORBIDDEN )
            routine_details_serializer = serializers.RoutineSerializer( get_routine_details, data = request.data, context = {'request': request}, partial = True)
            if routine_details_serializer.is_valid():
                routine_details_serializer.save()
                return Response({"message": routine_details_serializer.data,}, status=status.HTTP_201_CREATED)
        return Response({"message":routine_details_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class RoutineTaskAPIView(APIView):
    permission_classes =[IsAuthenticated]
    def post(self, request, routine_slug):
        get_routine = Routine.objects.get(slug = routine_slug)
        serializer = serializers.TodoSerializer(data = request.data, context={'request':request, 'routine_slug': routine_slug})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": serializer.data,}, status=status.HTTP_201_CREATED)
        return Response({"message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, routine_slug):
        get_routine_details = Routine.objects.get(slug = routine_slug)
        get_routine = Todo.objects.get(details = get_routine_details)
        serializer = serializers.TodoSerializer(get_routine)
        return Response({"data": serializer.data, "message": "successful"})

    def patch(self, request, routine_slug):
        try:
            get_routine = Todo.objects.get(details__slug=routine_slug)
        except ObjectDoesNotExist:
            return Response({'message': "Task can't be found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            if request.user != get_routine.details.author:
                return Response({'message':'This can only be edited by the owner'},  status=status.HTTP_403_FORBIDDEN )
            serializer = serializers.TodoSerializer( get_routine, data = request.data, context={'request':request, 'routine_slug': routine_slug}, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": serializer.data,}, status=status.HTTP_201_CREATED)
        return Response({"message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class RoutinesAPIView(APIView):
    def get(self, request):
        instance = Routine.objects.filter(privacy = True)
        serializer = serializers.RoutineTrackerSerializer(instance, many = True)
        return Response({"message": serializer.data,}, status=status.HTTP_201_CREATED)
class DeleteRoutineApiView(APIView):
    permission_classes = [permissions.AccessPermission]
    def delete(self,request, routine_slug):

        try:
            get_routine_details = Routine.objects.get(slug=routine_slug)
        except ObjectDoesNotExist:
            return Response({'message': "Routine can't be found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            if request.user != get_routine_details.author:
                return Response({'message':'This can only be edited by the owner'},  status=status.HTTP_403_FORBIDDEN )
            get_routine_details.delete()
            return Response("Routine deleted")

class MyRoutinesAPIView(APIView):
    permission_classes = [permissions.AccessPermission]
    def get(self, request):
        instance = Routine.objects.filter(author = request.user)
        task_instance = Todo.objects.filter (details__author = request.user)
        serializer =serializers.MyroutinesSerializer(instance, many = True)
        task_serializer = serializers.TodoSerializer(task_instance, many=True)
        # return Response({"Title Data":serializer.data,  "task Data":task_serializer.data})
        return Response({"message": serializer.data,}, status=status.HTTP_200_OK)


class TasksAPIView(APIView):
    permission_classes = [permissions.AccessPermission]
    def get(self, request, routine_slug):
        instance = Todo.objects.filter(details__slug = routine_slug)
        serializer =serializers.TodoSerializer(instance, many = True)
        return Response({"message": serializer.data,}, status=status.HTTP_200_OK)

class RoutineTrackerAPIView(APIView):
    def get(self, request, routine_slug = None):
        routines = RoutineTracker.objects.filter( user = request.user)
        serializer = serializers.GetRoutineTracker(routines, many = True)
        return Response(serializer.data)
    def post(self, request, routine_slug):
        routine = RoutineTracker.objects.get(routine__slug=routine_slug, user = request.user)
        if routine:
            return Response("Already Tracking this routine", status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.RoutineTrackerSerializer(data = request.data, context = {"request": request, "routine_slug":routine_slug})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class PrivacyAPIView(APIView):
    def post(self, request, routine_slug):
        privacy_status = Routine.objects.get(slug = routine_slug)
        response = request.data.get("privacy", "Private")
        small_char = response.lower()
        if small_char == 'private':
            privacy_status.privacy = False
            privacy_status.save()
        elif small_char == 'public':
            privacy_status.privacy = True
            privacy_status.save()
        else:
            return response (status.HTTP_400_BAD_REQUEST)
        return Response (response)
