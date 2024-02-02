from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import permissions, viewsets
from .serializers import TodoSerializer
from .models import Todo
from django.core import serializers

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    permission_classes = [] # [permissions.IsAuthenticated] => just for authentificated users
    
    
    def create(self, request):
        todo = Todo.objects.create(title=request.data.get('title', ''),
                                   description=request.data.get('description', ''),
                                   user=request.user
                                   )
        serialized_obj = serializers.serialize('json', [todo])
        return HttpResponse(serialized_obj, content_type='application/json')