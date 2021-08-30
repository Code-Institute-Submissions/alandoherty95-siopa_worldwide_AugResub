from django.urls import path
from . import views


# Home app URLs
urlpatterns = [
    path('', views.index, name='home')
]
