"""helloapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import json

from django.contrib import admin
from django.http import JsonResponse
from django.urls import path
from django.views import View
from django.utils.decorators import method_decorator
from helloapp.services import create_doctor , create_pacient , create_task
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name="dispatch")
class doctor(View):
    def get(self, request):
        person = '123'
        resp = {"success": False, "error": "No such user or user not set phone number."}
        if person:
            resp = {"success": True, "person": person}
        return JsonResponse(resp)

    def post(self, request):
        data = json.loads(request.body)
        create_doctor(data["name"], data["birthday"], data["phone"], data["email"], data["depart"], data["cab"],
                      data["startwork"], data["endwork"], data["vacation "])
        resp = {"success": True}
        return JsonResponse(resp)


@method_decorator(csrf_exempt, name="dispatch")
class pacient(View):
    def get(self, request):
        person = '123'
        resp = {"success": False, "error": "No such user or user not set phone number."}
        if person:
            resp = {"success": True, "person": person}
        return JsonResponse(resp)

    def post(self, request):
        data = json.loads(request.body)
        create_pacient(data["name"], data["birthday"], data["phone"], data["email"], data["depart"], data["chamber"],
                      data["starttreament"], data["endtreament"], data["checkout"])
        resp = {"success": True}
        return JsonResponse(resp)

@method_decorator(csrf_exempt, name="dispatch")
class task(View):
    def get(self, request):
        person = '123'
        resp = {"success": False, "error": "No such user or user not set phone number."}
        if person:
            resp = {"success": True, "person": person}
        return JsonResponse(resp)

    def post(self, request):
        data = json.loads(request.body)
        create_task(data["title"], data["description"], data["doctor"], data["time"])
        resp = {"success": True}
        return JsonResponse(resp)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pacient/', pacient.as_view()),
    path('doctor/', doctor.as_view()),
    path('task/', task.as_view()),
]
