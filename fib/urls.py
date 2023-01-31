from django.urls import path
from . import views

urlpatterns = [
    path('fib/<str:n>/', views.fibonacci_view, name='fibonacci'),
]