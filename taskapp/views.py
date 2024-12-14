from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from taskapp.models import Task
from django.contrib.auth import login,logout,authenticate
from rest_framework.response import Response
from rest_framework import status
from taskapp.serializers import RegisterSerializer, TaskSerializer

# Create your views here.

#VIEWSETS AUTOMATICALLY HEP US ADD CREATE, UPDATE AND DELETE TO VIEWS
class TaskViewSets(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def update(self, request, *args, **kwargs):
        task = self.get_object()
        if 'complete' in request.data:
            task.complete = request.data['complete']
            if task.complete:
                task.status = Task.COMPLETED
            else:
                task.status = Task.PENDING
            task.save()
        return super().update(request, *args, **kwargs)
        
class RegisterView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user=user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
        
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)