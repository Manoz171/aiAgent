from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def agent_home(request):
    return JsonResponse({
        "success": True,
        "message": "Django backend is running!"
    })