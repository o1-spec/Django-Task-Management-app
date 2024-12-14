from django.urls import path, include
from rest_framework.routers import DefaultRouter
from taskapp.views import TaskViewSets, RegisterView, LoginView, LogoutView

router = DefaultRouter()
router.register(r'tasks', TaskViewSets, basename='task')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]