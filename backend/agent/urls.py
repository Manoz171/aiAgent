from django.urls import path
from .views import home, agent_home

urlpatterns = [
    path("", home),
    path("api/", agent_home),
]