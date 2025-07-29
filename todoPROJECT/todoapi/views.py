from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskListSerializer, TaskDetailSerializer
from django.contrib.auth.models import User
# Create your views here.

class TodoSystem(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Task.objects.get(pk=pk, user=user)
        except Task.DoesNotExist:
            return None
        
    def get(self, request, pk=None):
        if pk:
            task = self.get_object(pk, request.user)
            if not task:
                return Response({'error':'Not found.'}, status=status.HTTP_404_NOT_FOUND)
            serializer = TaskDetailSerializer(task)
            return Response(serializer.data)
        
        tasks = Task.objects.filter(user=request.user)
        status_param = request.query_params.get('status')
        if status_param is not None:
            tasks = tasks.filter(status=status_param)
        serializer = TaskListSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TaskDetailSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        task = self.get_object(pk, request.user)
        serializer = TaskDetailSerializer(task, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error' : 'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk, request.user)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

