from rest_framework import generics, permissions
from .models import Expense
from .serializers import ExpenseSerializer
from .permissions import IsOwner


class ListExpense(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        user = self.request.user
        return Expense.objects.filter(user=user)


class DetailExpense(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwner,)
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
