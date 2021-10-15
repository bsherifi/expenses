# expenses/urls.py

from django.urls import path
from .views import ListExpense, DetailExpense

urlpatterns = [
    path('<int:pk>/', DetailExpense.as_view()),
    path('', ListExpense.as_view()),
]
