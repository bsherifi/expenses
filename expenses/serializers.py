# expenses/serializers.py
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('id', 'user', 'title', 'body', 'amount', 'date', 'created_at')
        read_only_fields = ('user', )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)
