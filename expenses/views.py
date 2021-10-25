# expenses/views.py
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Expense
from .serializers import ExpenseSerializer, UserSerializer
from .permissions import IsOwner


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsOwner]
