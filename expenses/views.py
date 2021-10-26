# expenses/views.py
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Expense
from .permissions import IsSuperUser, IsOwnUser, NotAllowed
from .serializers import ExpenseSerializer, UserSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [IsSuperUser, ]
        elif self.action == 'retrieve':
            self.permission_classes = [IsOwnUser, ]
        elif self.action == 'create':
            self.permission_classes = [NotAllowed, ]

        return super(self.__class__, self).get_permissions()
