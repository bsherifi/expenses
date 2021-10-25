# expenses/urls.py

from django.urls import path
from .views import UserViewSet, ExpenseViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', ExpenseViewSet, basename='expenses')

urlpatterns = router.urls
