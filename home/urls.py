from django.urls import path
from . import views

# DJANGO URL PATTERNS

urlpatterns = [
    path('', views.index, name='home')
]
