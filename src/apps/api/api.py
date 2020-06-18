from rest_framework import permissions
from rest_framework import viewsets

from .models import Category
from .models import Todo
from .serializers import CategorySerializer
from .serializers import TodoSerializer


# Todo ViewSet
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TodoSerializer


# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer
